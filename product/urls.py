from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<slug:productID>/', views.product, name="productInfo"),
    path('<slug:productID>/review/', views.productReview, name="productReview"),
]
