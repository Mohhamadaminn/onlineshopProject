from django.contrib import admin
from django.urls import path

from .views import productListView


urlpatterns = [
    path('', productListView.as_view(), name='product_list')
]