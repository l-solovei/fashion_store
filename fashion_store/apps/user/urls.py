from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from .views import UserCreateView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('signup/', UserCreateView.as_view(), name='create_user'),
    path('profile/', UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user_profile'),
]
