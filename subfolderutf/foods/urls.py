from django.urls import path
from .views import FoodListView

urlpatterns = [
    path('foods/', FoodListView.as_view(), name='food-list'),  # Обратите внимание на слэш в конце
]