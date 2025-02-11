from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategory
from .serializers import FoodListSerializer

class FoodListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()

        serializer = FoodListSerializer(categories, many=True)

        return Response(serializer.data)
