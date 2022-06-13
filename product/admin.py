from django.contrib import admin
from product.models import OrderItem, OrderBox, Product, Category, Comment, Rate

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(OrderBox)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rate)