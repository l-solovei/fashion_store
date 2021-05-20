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


class ProductPropertySerializer(ModelSerializer):
    # product = ProductSerializer(source='ProductModel', required=False)
    # color = ColorSerializer(source='ColorModel', required=False)

    class Meta:
        model = ProductPropertyModel
        fields = '__all__'
        extra_kwargs = {'product': {'read_only': True}}

    def create(self, validated_data):
        product = validated_data.pop('product')
        color = validated_data.pop('color')

        product_property = ProductPropertyModel.objects.create(product=product, color=color, **validated_data)
        product_property.save()

        return product_property

    def update(self, instance, validated_data):
        color = validated_data.pop('color')

        instance.size = validated_data.get('size', instance.size)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save

        color_serializer = ColorSerializer(data=color)
        if color_serializer.is_valid():
            color_serializer.update(instance=instance.color, validated_data=color_serializer.validated_data)

        return instance


class ProductSerializer(ModelSerializer):
    # PROBLEM - не обирає, а створює новий об'єкт, треба робити перевірку чи є такий в БД
    # brand_name = BrandSerializer(source='BrandModel', required=False)
    # cloth_type = ClothTypeSerializer(source='ClothTypeModel', required=False)
    # material = MaterialSerializer(source='MaterialModel', required=False)
    # owner = UserSerializer(source='UserModel', required=False)

    product_property = ProductPropertySerializer(many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}

    def create(self, validated_data):
        brand_name = validated_data.pop('brand_name')
        cloth_type = validated_data.pop('cloth_type')
        material = validated_data.pop('material')
        owner = validated_data.pop('owner')
        product_properties = validated_data.pop('product_property')

        product = ProductModel.objects.create(brand_name=brand_name, cloth_type=cloth_type, material=material,
                                              owner=owner, **validated_data)

        for product_property in product_properties:
            ProductPropertyModel.objects.create(product=product, **product_property)

        return product

    def update(self, instance, validated_data):
        brand_name = validated_data.pop('brand_name')
        cloth_type = validated_data.pop('cloth_type')
        material = validated_data.pop('material')
        # owner = validated_data.pop('owner') can`t update

        product_properties_data = validated_data.pop('product_property')
        product_property = (instance.product_property).all()
        product_property = list(product_property)

        instance.name = validated_data.get('name', instance.name)
        instance.basic_price = validated_data.get('basic_price', instance.basic_price)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.description = validated_data.get('description', instance.description)

        brand_name_serializer = BrandSerializer(data=brand_name)  # don`t update
        if brand_name_serializer.is_valid():
            brand_name_serializer.update(instance=instance.brand_name,
                                         validated_data=brand_name_serializer.validated_data)

        cloth_type_serializer = ClothTypeSerializer(data=cloth_type)
        if cloth_type_serializer.is_valid():
            cloth_type_serializer.update(instance=instance.cloth_type,
                                         validated_data=cloth_type_serializer.validated_data)

        material_serializer = MaterialSerializer(data=material)
        if material_serializer.is_valid():
            material_serializer.update(instance=instance.material,
                                       validated_data=material_serializer.validated_data)

        for product_property_data in product_properties_data:
            product_property_serializer = ProductPropertySerializer(data=product_property_data)
            if product_property_serializer.is_valid():
                product_property_serializer.update(instance=instance.product_property,
                                                   validated_data=product_property_serializer.validated_data)
            #product_property.update(product_property_data)
            # product_property.size = product_property_data.get('size', product_property.size)
            # product_property.quantity = product_property_data.get('quantity', product_property.quantity)
            # # product_property.color = product_property_data.pop('color')
            # #
            # # color_serializer = ColorSerializer(data= product_property.color)
            # # if color_serializer.is_valid():
            # #     color_serializer.update()

            product_property.save()

        instance.save()

        return instance
