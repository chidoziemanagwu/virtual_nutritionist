from rest_framework import serializers
from .models import UserProfile, MealPlan, DailyNutritionCheckIn

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'


class DailyNutritionCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNutritionCheckIn
        fields = '__all__'
        read_only_fields = ('user', 'created_at')