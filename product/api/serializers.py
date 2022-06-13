from dataclasses import fields
from rest_framework import serializers
from product.models import Product, OrderItem, OrderBox, ProductImage, Rate, Comment, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    review_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Rate
        fields = '__all__'
        
        
class RateListSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField()
    
    class Meta:
        model = Rate
        fields = '__all__'    
        
    def get_customer(self, obj):
        return obj.review_user.username  
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = instance.product.name
        return rep          
        
        
class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = instance.product.name
        return rep 
        

class CommentListSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField()
    product = serializers.StringRelatedField(source='product.name')
    
    class Meta:
        model = Comment
        fields = '__all__'    
        
    def get_customer(self, obj):
        return obj.comment_user.username


class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ['images',]

class ProductSerializer(serializers.ModelSerializer):
    rate = RateSerializer(many=True, read_only=True)    
    comment = CommentSerializer(many=True, read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.name
        return rep     


class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = "__all__"
        

class OrderItemCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = "__all__"
            
    
class OrderBoxListSerializer(serializers.ModelSerializer):
    orderitems = OrderItemListSerializer(many=True)
    customer = serializers.StringRelatedField()
    
    class Meta:
        model = OrderBox
        fields = '__all__'
        
    def get_customer(self, obj):
        return obj.customer.username
    

class OrderBoxCreateSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = OrderBox
        fields = '__all__'
