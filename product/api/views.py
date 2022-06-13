from rest_framework.exceptions import ValidationError
from rest_framework import generics
from product.models import OrderBox, Product, ProductImage, Category, OrderItem, Rate, Comment
from product.api.serializers import CategorySerializer, OrderItemListSerializer, ProductSerializer, ProductImageSerializer, \
                                    OrderItemCreateSerializer, OrderBoxListSerializer, OrderBoxCreateSerializer, \
                                    RateSerializer, RateListSerializer, CommentSerializer, CommentListSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
    

class ProductMoreImageCreateAPIView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        product = Product.objects.get(pk=pk)
        
        serializer.save(images=serializer.validated_data['images'], product=product)
    

class ProductMoreImageDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
    
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]


class OrderItemListAPIView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer
    
    permission_classes = [IsAuthenticated]
    

class OrderItemCreateAPIView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateSerializer
    
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        queryset = OrderItem.objects.filter(order_box_id=serializer.validated_data['order_box'], product_id=serializer.validated_data['product'])
        
        if queryset.exists():
            raise ValidationError("This product is already exists in your card box")
        
        serializer.save()
        
    
class OrderItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class OrderBoxListAPIView(generics.ListAPIView):
    queryset = OrderBox.objects.all()
    serializer_class = OrderBoxListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer__username',]
    
    permission_classes = [IsAuthenticated]


class OrderBoxCreateAPIView(generics.CreateAPIView):
    queryset = OrderBox.objects.all()
    serializer_class = OrderBoxCreateSerializer
    
    permission_classes = [IsAuthenticated]  
      
      
class OrderBoxDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderBox.objects.all()
    serializer_class = OrderBoxCreateSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]


class RateListAPIView(generics.ListAPIView):
    serializer_class = RateListSerializer
    queryset = Rate.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id',]
    

class RateCreateAPIView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        
        review_user = self.request.user
        queryset = Rate.objects.filter(review_user=review_user, product=product)
        
        if queryset.exists():
            raise ValidationError("You have already send your product rate, that's enough dude!.")
        
        return serializer.save()
    

class RateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer   
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        product = Product.objects.get(id=pk)
        
        comment_user = self.request.user
        queryset = Comment.objects.filter(comment_user__username=comment_user, product=product)
        
        if queryset.exists():
            raise ValidationError("You have already send your comment, that's enough dude!.")
        
        return serializer.save()
    

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id',]
    
    
class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = [IsAuthenticatedOrReadOnly]