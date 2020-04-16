
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import DishViewSet

router = routers.DefaultRouter()
router.register('dish', DishViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('powitanie/', views.pierwsza, name='pierwsza'),
    path('auth/', obtain_auth_token),

]