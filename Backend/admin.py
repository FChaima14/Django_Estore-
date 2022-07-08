from django.contrib import admin

from .models import Product, OrderItem, Order, Customer, ShippingAddress

admin.site.register(Product);
admin.site.register(Order);
admin.site.register(OrderItem);
admin.site.register(Customer);
admin.site.register(ShippingAddress);

# Register your models here.
