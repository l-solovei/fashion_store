from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class RecipientCreateAPIView(CreateAPIView):
    serializer_class = RecipientSerializer
    queryset = RecipientModel.objects.all()
    permission_classes = (IsAuthenticated,)


# може і не треба того
# class RecipientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     Model = RecipientModel
#     serializer_class = RecipientSerializer
#     queryset = RecipientModel.objects.all
#     permission_classes = (IsAuthenticated,) #до того моменту, поки не підтвердив замовлення
#     http_method_names = ['get', 'patch', 'delete']


class SelectedProductListCreateAPIView(ListCreateAPIView):
    serializer_class = SelectedProductSerializer
    queryset = SelectedProductsModel.objects.all()
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # описати доступні продукти+якщо попадає в корзину, то віднімати зі складу
        pass

    def perform_create(self, serializer):
        serializer.save(product=self.request.product,
                        size=self.request.product.size,
                        color=self.request.product.color)


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = OrderModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
