from django.db import models

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
