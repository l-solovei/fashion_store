from django.db import models
from django.core.validators import MinValueValidator

from utils.abstract_models import CreateUpdateModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class BrandModel(CreateUpdateModel):
    brand_name = models.CharField(max_length=50, unique=True,
                                  verbose_name='Brand')

    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ('brand_name',)

    def __str__(self):
        return f'{self.brand_name}'


class ColorModel(CreateUpdateModel):
    color_name = models.CharField(max_length=20, unique=True,
                                  verbose_name='Color Name')
    color_hex = models.CharField(max_length=20, unique=True,
                                 verbose_name='Color Hex')

    class Meta:
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        ordering = ('color_name',)

    def __str__(self):
        return f'{self.color_name}'


class MaterialModel(CreateUpdateModel):
    material = models.CharField(max_length=20, unique=True,
                                verbose_name='Material')

    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ('material',)

    def __str__(self):
        return f'{self.material}'


class ClothTypeModel(CreateUpdateModel):
    cloth_type = models.CharField(max_length=20, unique=True,
                                  verbose_name='Material')

    class Meta:
        db_table = 'cloth_type'
        verbose_name = 'Cloth type'
        verbose_name_plural = 'Cloth types'
        ordering = ('cloth_type',)

    def __str__(self):
        return f'{self.cloth_type}'


class ProductModel(CreateUpdateModel):
    man = 'Man'
    woman = 'Woman'
    kids = 'Kids'

    gender_choices = [
        (man, 'Man'),
        (woman, 'Woman'),
        (kids, 'Kids')
    ]

    name = models.CharField(max_length=50, verbose_name='Name')
    brand_name = models.ManyToManyField(BrandModel, verbose_name='Brand')
    basic_price = models.FloatField(validators=[MinValueValidator(0.0)],
                                    verbose_name='Basic Prise')
    gender = models.CharField(max_length=5, choices=gender_choices,
                              verbose_name='Gender')
    description = models.TextField(verbose_name='Description')
    cloth_type = models.ForeignKey(ClothTypeModel, on_delete=models.CASCADE,
                                   related_name='product_cloth_type',
                                   verbose_name='ClothType')
    material = models.ForeignKey(MaterialModel, on_delete=models.CASCADE,
                                 related_name='product_material',
                                 verbose_name='Material')
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} - {self.basic_price}'


class ProductPropertyModel(CreateUpdateModel):
    s = 'S'
    m = 'M'
    l = 'L'
    xl = 'XL'
    xxl = 'XXL'

    size_choices = [
        (s, 'S'),
        (m, 'M'),
        (l, 'L'),
        (xl, 'XL'),
        (xxl, 'XXL')
    ]
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    size = models.CharField(max_length=3, choices=size_choices,
                            verbose_name='Size')
    color = models.OneToOneField(ColorModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', null=True,
                              verbose_name='Image')
    # images = ArrayField(
    #     models.ForeignKey(ImageModel, on_delete=models.CASCADE))
