from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    images = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   
    def __str__(self):
        return self.product.name
    
class OrderBox(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    orderbox_data = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_products')
    order_box = models.ForeignKey(OrderBox, on_delete=models.CASCADE, related_name='orderitems')
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + ' | OrderItem ' + str(self.product.name)
    

class Rate(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rate')
    rate = models.PositiveIntegerField(default=0,
        validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    
    def __str__(self):
        return str(self.id) + ' | ReviewUser ' + str(self.review_user) + ' | Rate ' + str(self.rate)
    

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField(max_length=300)
    
    def __str__(self):
        return str(self.id) + ' | CommentUser ' + str(self.comment_user)