from django.urls import path

from .views import *

urlpatterns = [
    path('create_brand/', BrandCreateAPIView.as_view(), name='create_brand'),
    path('delete_brand/<int:pk>/', BrandDestroyAPIView.as_view(),
         name='delete_brand'),

    path('create_color/', ColorCreateAPIView.as_view(), name='create_color'),
    path('delete_color/<int:pk>/', ColorDestroyAPIView.as_view(),
         name='delete_color'),

    path('create_material/', MaterialCreateAPIView.as_view(),
         name='create_material'),
    path('delete_material/<int:pk>/', MaterialDestroyAPIView.as_view(),
         name='delete_material'),

    path('create_cloth_type/', ClothTypeCreateAPIView.as_view(),
         name='create_cloth_type'),
    path('delete_cloth_type/<int:pk>/', ColorDestroyAPIView.as_view(),
         name='delete_delete_material'),

    path('', ProductListCreateAPIView.as_view(),
         name='list_create_product'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='retrieve_update_delete_product'),

    # path('<int:pk>/property/', ProductPropertyCreateAPIView.as_view(),
    #      name='create_product_property'), #do it in product
]
