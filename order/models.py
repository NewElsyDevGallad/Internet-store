from django.db import models
from shop.models import Product


class ShopClient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=127)
    street = models.CharField(max_length=127)
    house = models.CharField(max_length=127, blank=True, null=True)

    class Meta:
        db_table = "Client"
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class ClientBankAccount(models.Model):
    card_number = models.CharField(max_length=12, db_index=True, unique=True)
    card_holder = models.CharField(max_length=30)
    validity = models.DateField()
    cvc_code = models.CharField(max_length=3)

    class Meta:
        db_table = "ClientBankAccount"
        verbose_name = 'ClientBankAccount'
        verbose_name_plural = 'ClientBankAccounts'

    def __str__(self):
        return self.card_number


class ClientElectronWallet(models.Model):
    account_number = models.CharField(max_length=20, db_index=True, unique=True)
    account_holder = models.CharField(max_length=30)

    class Meta:
        db_table = "ClientElectronWallet"
        verbose_name = 'ClientElectronWallet'
        verbose_name_plural = 'ClientElectronWallets'

    def __str__(self):
        return self.account_number


class Delivery(models.Model):
    name = models.CharField(max_length=127, db_index=True, unique=True)
    cost = models.IntegerField()

    class Meta:
        db_table = "Delivery"
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=127, db_index=True, unique=True)

    class Meta:
        db_table = "Payment"
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.name


class ShopOrder(models.Model):
    client = models.ForeignKey(ShopClient, models.CASCADE)
    pay_method = models.ForeignKey(Payment, models.CASCADE)
    delivery = models.ForeignKey(Delivery, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = "Order"
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(ShopOrder, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "OrderItem"
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
