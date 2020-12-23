from django.contrib import admin
from .models import ShopClient, Delivery, Payment, ShopOrder, OrderItem, ClientBankAccount, ClientElectronWallet


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'pay_method', 'delivery', 'created', 'paid']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]


admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(ShopClient)
admin.site.register(ShopOrder, OrderAdmin)
admin.site.register(ClientBankAccount)
admin.site.register(ClientElectronWallet)
