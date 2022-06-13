from django.contrib import admin
from product.models import OrderItem, OrderBox, Product, ProductImage, Category, Comment, Rate

# Register your models here.
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    
    class Meta:
        model = Product
        
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderItem)
admin.site.register(OrderBox)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rate)