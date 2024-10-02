import os
from openai import OpenAI
from dotenv import load_dotenv
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from django import forms
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import UserProfile, MealPlan

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client using the API key from the environment

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Form for collecting user profile data
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'dietary_preferences', 'health_goals', 'calorie_limit']

# Function to generate meal plan and grocery list using OpenAI
def generate_meal_plan(user_profile):
    try:
        # Use OpenAI client to generate both meal plan and grocery list
        prompt = (
            f"Generate a meal plan for a {user_profile.age}-year-old who follows a {user_profile.dietary_preferences} diet "
            f"and wants to achieve {user_profile.health_goals}. The calorie limit is {user_profile.calorie_limit}. "
            f"Also provide a grocery list based on the meal plan."
        )

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo",
            max_tokens=500  # Adjust token limit as needed
        )

        # Extract the content
        meal_plan_response = response.choices[0].message.content

        # Split the response into meal plan and grocery list using markers
        if "Grocery List:" in meal_plan_response:
            meal_plan, grocery_list = meal_plan_response.split("Grocery List:")
        else:
            meal_plan = meal_plan_response
            grocery_list = "Not available."

        # Strip any excess whitespace
        return meal_plan.strip(), grocery_list.strip()

    except Exception as e:
        return str(e), ""

# HTML view to handle user profile creation and meal plan generation
# Updated form view to split the meal plan and grocery list into lists
class MealPlanFormView(FormView):
    template_name = 'mealplanner/user_profile.html'
    form_class = UserProfileForm
    success_url = '/'

    def form_valid(self, form):
        # Save the user profile
        user_profile = form.save()

        # Generate the meal plan and grocery list using OpenAI
        meal_plan_text, grocery_list = generate_meal_plan(user_profile)

        # Split the meal plan and grocery list into lists (assuming '-' separates items)
        meal_plan_items = [item.strip() for item in meal_plan_text.split('-') if item.strip()]
        grocery_list_items = [item.strip() for item in grocery_list.split('-') if item.strip()]

        # Save the meal plan and grocery list to the database
        meal_plan = MealPlan.objects.create(
            user=user_profile,
            meal_plan=meal_plan_text,
            grocery_list=grocery_list
        )

        return render(self.request, 'mealplanner/meal_plan_result.html', {
            'meal_plan': meal_plan,
            'user_profile': user_profile,
            'meal_plan_items': meal_plan_items,  # Pass the meal plan list
            'grocery_list_items': grocery_list_items  # Pass the grocery list
        })


# API to download the meal plan as a PDF
class DownloadMealPlanPDFView(FormView):
    def get(self, request, meal_plan_id):
        meal_plan = get_object_or_404(MealPlan, id=meal_plan_id)

        # Create a PDF response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="meal_plan_{meal_plan.id}.pdf"'

        # Generate the PDF
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