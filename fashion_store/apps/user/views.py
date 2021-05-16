from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    """Create user"""

    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Read, update and delete user"""

    model = UserModel
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user

        if user:
            return self.request.user
        else:
            return super().get_object()
