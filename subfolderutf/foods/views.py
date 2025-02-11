from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategory
from .serializers import FoodListSerializer

class FoodListView(APIView):
    def get(self, request, *args, **kwargs):
        # Фильтруем категории, у которых есть хотя бы одно блюдо с is_publish=True
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        
        # Сериализуем данные
        serializer = FoodListSerializer(categories, many=True)
        
        # Возвращаем JSON-ответ
        return Response(serializer.data)