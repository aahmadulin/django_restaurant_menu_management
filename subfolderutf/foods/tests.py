from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FoodCategory, Food

class FoodListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = FoodCategory.objects.create(name_ru='Напитки', order_id=10)
        self.food = Food.objects.create(
            category=self.category,
            name_ru='Чай',
            cost='123.00',
            is_publish=True
        )

    def test_food_list_view(self):
        url = reverse('food-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)