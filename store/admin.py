from django.contrib import admin
from store.models import Customer,OrderItem,ShippingAddress,Product,Order
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ShippingAddress)


