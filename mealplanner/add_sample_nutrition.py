from django.core.management.base import BaseCommand
from mealplanner.models import NutritionalInfo

class Command(BaseCommand):
    help = 'Add sample nutritional information for the six classes of food'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "food_name": "Apple",
                "category": "carbohydrates",
                "calories": 95,
                "protein": 0.3,
                "fat": 0.2,
                "carbohydrates": 25,
                "vitamins": "Vitamin C",
                "minerals": "Potassium",
                "water_content": 86
            },
            {
                "food_name": "Chicken Breast",
                "category": "proteins",
                "calories": 165,
                "protein": 31,
                "fat": 3.6,
                "carbohydrates": 0,
                "vitamins": "Vitamin B6",
                "minerals": "Phosphorus, Selenium",
                "water_content": 65
            },
            {
                "food_name": "Salmon",
                "category": "fats",
                "calories": 208,
                "protein": 20,
                "fat": 13,
                "carbohydrates": 0,
                "vitamins": "Vitamin D",
                "minerals": "Potassium",
                "water_content": 60
            },
            {
                "food_name": "Carrot",
                "category": "vitamins",
                "calories": 41,
                "protein": 0.9,
                "fat": 0.2,
                "carbohydrates": 10,
                "vitamins": "Vitamin A, Vitamin K1",
                "minerals": "Potassium",
                "water_content": 88
            },
            {
                "food_name": "Spinach",
                "category": "minerals",
                "calories": 23,
                "protein": 2.9,
                "fat": 0.4,
                "carbohydrates": 3.6,
                "vitamins": "Vitamin A, Vitamin C, Vitamin K",
                "minerals": "Iron, Magnesium",
                "water_content": 91
            },
            {
                "food_name": "Watermelon",
                "category": "water",
                "calories": 30,
                "protein": 0.6,
                "fat": 0.2,
                "carbohydrates": 8,
                "vitamins": "Vitamin A, Vitamin C",
                "minerals": "Potassium",
                "water_content": 92
            }
        ]

        for item in sample_data:
            NutritionalInfo.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Sample nutritional data for six food classes added!'))
