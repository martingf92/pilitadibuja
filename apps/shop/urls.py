from django.urls import path

from .views import ListProducts

urlpatterns = [
    path('', ListProducts.as_view(), name='shop'),
]
