from django.db import models
from django.contrib.auth.models import User

# Food Categories for the six classes of food
FOOD_CATEGORIES = [
    ('carbohydrates', 'Carbohydrates'),
    ('proteins', 'Proteins'),
    ('fats', 'Fats'),
    ('vitamins', 'Vitamins'),
    ('minerals', 'Minerals'),
    ('water', 'Water'),
]

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dietary_preferences = models.TextField()  # e.g., vegan, keto, etc.
    health_goals = models.TextField()  # e.g., weight loss, muscle gain
    calorie_limit = models.IntegerField()

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    meal_plan = models.TextField()
    grocery_list = models.TextField()
    pdf_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name}'s Meal Plan"

# Model for Nutritional Information
class NutritionalInfo(models.Model):
    food_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=FOOD_CATEGORIES)  # Class of food
    calories = models.FloatField()
    protein = models.FloatField(null=True, blank=True)  # grams of protein
    fat = models.FloatField(null=True, blank=True)  # grams of fat
    carbohydrates = models.FloatField(null=True, blank=True)  # grams of carbohydrates
    vitamins = models.TextField(null=True, blank=True)  # Vitamins (A, B, C, etc.)
    minerals = models.TextField(null=True, blank=True)  # Minerals (Calcium, Iron, etc.)
    water_content = models.FloatField(null=True, blank=True)  # Water content in grams

    def __str__(self):
        return self.food_name





class UserStreak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='streak')
    current_streak = models.PositiveIntegerField(default=1)
    longest_streak = models.PositiveIntegerField(default=1)
    last_logged_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.current_streak} Day Streak"

class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="CSS icon class or filename")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'badge')

    def __str__(self):
        return f"{self.user.username} unlocked {self.badge.name}"
