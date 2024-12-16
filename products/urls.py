from django.contrib import admin
from django.urls import path

from .views import productListView, productDetailView


urlpatterns = [
    path('', productListView.as_view(), name='product_list'),
    path('<int:pk>', productDetailView.as_view(), name='product_detail'),
]