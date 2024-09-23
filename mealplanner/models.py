from django.db import models

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
