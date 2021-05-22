from rest_framework.serializers import ModelSerializer

from .models import *
from ..product.serializers import ProductSerializer
from ..user.serializers import UserSerializer


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = RecipientModel
        fields = ['first_name', 'last_name', 'email', 'city', 'state',
                  'street', 'phone', 'zip']


class SelectedProductSerializer(ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = SelectedProductsModel
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    products = SelectedProductSerializer(many=True)
    recipient = RecipientSerializer(many=False)

    class Meta:
        model = OrderModel
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        recipient = validated_data.pop('recipient')
        user = validated_data.pop('user')
        products = validated_data.pop('products')

        order = OrderModel.objects.create(user=user, **validated_data)

        recipient = RecipientModel.objects.create(**recipient)
        for product in products:
            SelectedProductsModel.objects.create(order=order, **product)

        order.save()

        return order
