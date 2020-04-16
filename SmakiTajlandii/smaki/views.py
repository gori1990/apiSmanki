from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

from .models import Dish
from rest_framework import viewsets
from .serializers import DishSerializer, DishMiniSerializer


def pierwsza(request):
    return HttpResponse("Witamy w Smakach Tajlandii")


class DishViewSet(viewsets.ModelViewSet,):
    serializer_class = DishMiniSerializer
    queryset = Dish.objects.all()

    def retrieve(self, request, *args, **kwargs, ):
        dish = self.get_object()
        serializer = DishSerializer(dish)
        return Response(serializer.data)



