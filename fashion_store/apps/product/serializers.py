from rest_framework.serializers import ModelSerializer

from .models import BrandModel, ColorModel, MaterialModel, ClothTypeModel, \
    ProductModel, ProductPropertyModel
from ..user.serializers import UserSerializer


class BrandSerializer(ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class ColorSerializer(ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = MaterialModel
        fields = '__all__'


class ClothTypeSerializer(ModelSerializer):
    class Meta:
        model = ClothTypeModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    brand_name = BrandSerializer(source='BrandModel', required=False)
    cloth_type = ClothTypeSerializer(source='ClothTypeModel', required=False)
    material = MaterialSerializer(source='MaterialModel', required=False)
    owner = UserSerializer(source='UserModel', required=False)

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductPropertySerializer(ModelSerializer):
    product = ProductSerializer(source='ProductModel', required=False)
    color = ColorSerializer(source='ColorModel', required=False)

    class Meta:
        model = ProductPropertyModel
        fields = '__all__'
