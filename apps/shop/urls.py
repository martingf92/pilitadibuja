from django.urls import path

from . import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
    path('shop/category/<str:category>', views.shop, name='filter_by_plant_category'),
    path('shop/<int:pk>', views.product_detail, name='product_detail'),
]