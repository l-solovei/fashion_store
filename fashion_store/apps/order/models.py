from django.db import models
from phone_field import PhoneField
from django.contrib.auth import get_user_model


from fashion_store.apps.product.models import ProductModel
from fashion_store.apps.product.models import ColorModel
from utils.abstract_models import CreateUpdateModel


UserModel = get_user_model()


class RecipientModel(UserModel):
    street = models.CharField(max_length=50, verbose_name='State')
    phone = PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        db_table = 'recipient'
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'
        # ordering = ('',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OrderModel(CreateUpdateModel):
    completed = 'Completed'
    opened = 'Opened'
    canceled = 'Canceled'
    processed = 'Processed'

    status_choices = [
        (completed, 'Completed'),
        (opened, 'Opened'),
        (canceled, 'Canceled'),
        (processed, 'Processed')
    ]

    total_price = models.FloatField(verbose_name='Total price')
    status = models.CharField(max_length=10, choices=status_choices,
                              default='Opened', verbose_name='Status')
    hide = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                             related_name='order_user',
                             verbose_name='User')
    recipient = models.OneToOneField(RecipientModel, on_delete=models.CASCADE,
                                     related_name='order_recipient',
                                     verbose_name='Recipient')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        # ordering = ('',)

    # def __str__(self):
    #     pass


class SelectedProductsModel(CreateUpdateModel):
    order = models.ForeignKey(OrderModel, verbose_name='Order',
                              on_delete=models.SET_NULL, null=True)
    color = models.OneToOneField(ColorModel, verbose_name='Color',
                                 on_delete=models.CASCADE, )
    size = models.CharField(max_length=3)
    product = models.ForeignKey(ProductModel, verbose_name='Product',
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
