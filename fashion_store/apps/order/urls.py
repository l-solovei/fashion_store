from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderCreateAPIView.as_view(), name='create_order'),

    path('selected_product/<int:pk>/',
         SelectedProductListCreateAPIView.as_view(), name='selected_product'),

    path('<int:pk>/recipient/', RecipientCreateAPIView.as_view(),
         name='recipient')
]
