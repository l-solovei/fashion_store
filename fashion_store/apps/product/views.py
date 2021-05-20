from rest_framework.generics import CreateAPIView, DestroyAPIView, \
    ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .models import BrandModel, ColorModel, MaterialModel, ClothTypeModel, \
    ProductModel
from .serializers import BrandSerializer, ColorSerializer, MaterialSerializer, \
    ClothTypeSerializer, ProductSerializer, ProductPropertySerializer


class BrandCreateAPIView(CreateAPIView):
    """Only admin can create brand"""

    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class BrandDestroyAPIView(DestroyAPIView):
    """Only admin can delete brand"""

    serializer_class = BrandSerializer
    queryset = BrandModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class ColorCreateAPIView(CreateAPIView):
    """Only admin can create color"""

    serializer_class = ColorSerializer
    queryset = ColorModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class ColorDestroyAPIView(DestroyAPIView):
    """Only admin can delete color"""

    serializer_class = ColorSerializer
    queryset = ColorModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class MaterialCreateAPIView(CreateAPIView):
    """Only admin can create material"""

    serializer_class = MaterialSerializer
    queryset = MaterialModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class MaterialDestroyAPIView(DestroyAPIView):
    """Only admin can delete material"""

    serializer_class = MaterialSerializer
    queryset = MaterialModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class ClothTypeCreateAPIView(CreateAPIView):
    """Only admin can create cloth type"""

    serializer_class = ClothTypeSerializer
    queryset = ClothTypeModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class ClothTypeDestroyAPIView(DestroyAPIView):
    """Only admin can delete cloth type"""

    serializer_class = ClothTypeSerializer
    queryset = ClothTypeModel.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    #permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user #додати валідацію на бренди і т.д.
        )


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Read, update and delete user"""

    model = ProductModel
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    #permission_classes = (IsAuthenticated,) #IsProductOwner
    http_method_names = ['get', 'patch', 'delete']

    # def get_permissions(self):
    #
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     else:
    #         return [IsProductOwner()]


class ProductPropertyCreateAPIView(CreateAPIView):
    serializer_class = ProductPropertySerializer
    queryset = ProductModel.objects.all()
    #permission_classes = (IsAuthenticated,) #IsProductOwner

    def perform_create(self, serializer):
        product_id = self.kwargs.get('pk')
        #color_id = self.kwargs.get('pk')
        product = get_object_or_404(ProductModel, pk=product_id)
        #color = get_object_or_404(ColorModel, pk=color_id)
        serializer.save(product=product)#, color=color)
