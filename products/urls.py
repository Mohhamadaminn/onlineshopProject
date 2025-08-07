from django.contrib import admin
from django.urls import path

from .views import productListView, productDetailView, CommentCrateView


urlpatterns = [
    path('', productListView.as_view(), name='product_list'),
    path('<int:pk>/', productDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCrateView.as_view(), name='comment_create'),
]