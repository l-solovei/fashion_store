from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import BrandModel
from .serializers import BrandSerializer


class BrandCreate(CreateAPIView):
    """Only admin can create brand"""

    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class BrandDelete(DestroyAPIView):
    """Only admin can delete brand"""

    