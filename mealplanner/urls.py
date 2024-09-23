from django.urls import path
from .views import MealPlanFormView, DownloadMealPlanPDFView, MealPlanFormView

urlpatterns = [
    # HTML views
    path('', MealPlanFormView.as_view(), name='user_profile'),  # The form to create a user profile and generate a meal plan
    path('download-pdf/<int:meal_plan_id>/', DownloadMealPlanPDFView.as_view(), name='download_meal_plan_pdf'),  # Download the meal plan as a PDF
    
    # API views
    path('api/meal-plan/', MealPlanFormView.as_view(), name='api_meal_plan'),  # API to create a user profile and generate a meal plan
    path('api/meal-plan/download/<int:meal_plan_id>/', DownloadMealPlanPDFView.as_view(), name='download_meal_plan_pdf_api'),  # API to download the meal plan as PDF
]
