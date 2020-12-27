from django.contrib import admin
from django.urls import path, include
from app.views import ReviewEmailView
from .views import OrderListCreateView
import views
urlpatterns = [
    path('', OrderListCreateView.as_view(), name='cafe'),
    path('meal/<int:id>/', views.meal_detail, name='meal_detail'),
]
