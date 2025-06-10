import os
from datetime import date, timedelta
from dotenv import load_dotenv
from openai import OpenAI

from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timezone
from .models import Badge, MealPlan, NutritionalInfo, UserBadge, UserProfile, UserStreak, DailyNutritionCheckIn
from .serializers import DailyNutritionCheckInSerializer
from .models import Badge, MealPlan, NutritionalInfo, UserBadge, UserProfile, UserStreak

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Form for collecting user profile data
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'dietary_preferences', 'health_goals', 'calorie_limit']


# Helper function to generate meal plan and grocery list
def generate_meal_plan(user_profile):
    try:
        prompt = (
            f"Generate a meal plan for a {user_profile.age}-year-old who follows a {user_profile.dietary_preferences} diet "
            f"and wants to achieve {user_profile.health_goals}. The calorie limit is {user_profile.calorie_limit}. "
            f"Also provide a grocery list based on the meal plan."
        )

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo",
            max_tokens=500
        )

        meal_plan_response = response.choices[0].message.content

        if "Grocery List:" in meal_plan_response:
            meal_plan, grocery_list = meal_plan_response.split("Grocery List:")
        else:
            meal_plan = meal_plan_response
            grocery_list = "Not available."

        return meal_plan.strip(), grocery_list.strip()

    except Exception as e:
        return str(e), ""


# Form View to handle user profile creation and meal plan display
class MealPlanFormView(FormView):
    template_name = 'mealplanner/user_profile.html'
    form_class = UserProfileForm
    success_url = '/'

    def form_valid(self, form):
        user_profile = form.save()
        meal_plan_text, grocery_list = generate_meal_plan(user_profile)

        meal_plan_items = [item.strip() for item in meal_plan_text.split('-') if item.strip()]
        grocery_list_items = [item.strip() for item in grocery_list.split('-') if item.strip()]

        meal_plan = MealPlan.objects.create(
            user=user_profile,
            meal_plan=meal_plan_text,
            grocery_list=grocery_list
        )

        return render(self.request, 'mealplanner/meal_plan_result.html', {
            'meal_plan': meal_plan,
            'user_profile': user_profile,
            'meal_plan_items': meal_plan_items,
            'grocery_list_items': grocery_list_items
        })


def nutritional_info_list(request):
    nutritional_info = NutritionalInfo.objects.all()
    return render(request, 'mealplanner/nutritional_info_list.html', {'nutritional_info': nutritional_info})


# View to generate and download meal plan PDF
class DownloadMealPlanPDFView(FormView):
    def get(self, request, meal_plan_id):
        meal_plan = get_object_or_404(MealPlan, id=meal_plan_id)

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pdfmetrics.registerFont(TTFont('NotoColorEmoji', os.path.join(base_dir, 'fonts', 'NotoColorEmoji-Regular.ttf')))

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="meal_plan_{meal_plan.id}.pdf"'

        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 800, f"🥗 Meal Plan for {meal_plan.user.name}")
        
        p.setFont("Helvetica", 12)
        p.drawString(100, 780, f"🍎 Dietary Preferences: {meal_plan.user.dietary_preferences}")
        p.drawString(100, 760, f"🎯 Health Goals: {meal_plan.user.health_goals}")
        p.drawString(100, 740, f"🔥 Calorie Limit: {meal_plan.user.calorie_limit} kcal")

        p.drawString(100, 700, "🍽️ Meal Plan:")
        p.drawString(100, 680, meal_plan.meal_plan)

        p.drawString(100, 650, "🛒 Grocery List:")
        p.drawString(100, 630, meal_plan.grocery_list)

        p.showPage()
        p.save()

        return response


# Gamification API Endpoint
class GamificationStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        streak, created = UserStreak.objects.get_or_create(user=request.user)

        if not created:
            if streak.last_logged_date == today - timedelta(days=1):
                streak.current_streak += 1
                if streak.current_streak > streak.longest_streak:
                    streak.longest_streak = streak.current_streak
                streak.save()
            elif streak.last_logged_date < today - timedelta(days=1):
                streak.current_streak = 1
                streak.save()

        user_badges = UserBadge.objects.filter(user=request.user).select_related('badge')
        badges_data = [
            {
                "name": ub.badge.name,
                "description": ub.badge.description,
                "icon_name": ub.badge.icon_name,
                "earned_at": ub.earned_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            for ub in user_badges
        ]

        return Response({
            "current_streak": streak.current_streak,
            "longest_streak": streak.longest_streak,
            "last_logged_date": streak.last_logged_date,
            "earned_badges_count": len(badges_data),
            "badges": badges_data
        }, status=status.HTTP_200_OK)


class DailyNutritionCheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DailyNutritionCheckInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        checkin = serializer.save(user=request.user)
        log_date = checkin.log_date

        streak, created = UserStreak.objects.get_or_create(
            user=request.user,
            defaults={
                'current_streak': 1,
                'longest_streak': 1,
                'last_logged_date': log_date
            }
        )

        # Do not change streak if user is updating the same day
        if streak.last_logged_date != log_date:
            if streak.last_logged_date == log_date - timedelta(days=1):
                streak.current_streak += 1
            else:
                streak.current_streak = 1

            if streak.current_streak > streak.longest_streak:
                streak.longest_streak = streak.current_streak

            streak.last_logged_date = log_date
            streak.save()

        return Response({
            "message": "Daily check-in saved successfully.",
            "checkin": DailyNutritionCheckInSerializer(checkin).data,
            "current_streak": streak.current_streak,
            "longest_streak": streak.longest_streak
        }, status=status.HTTP_201_CREATED)