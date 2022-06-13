from django.urls import path, include
from product.api.views import CategoryViewSet, ProductListAPIView, ProductDetailAPIView, \
                              OrderItemListAPIView, OrderItemDetailAPIView, OrderItemCreateAPIView, \
                              OrderBoxListAPIView, OrderBoxCreateAPIView, OrderBoxDetailAPIView, \
                              RateListAPIView, RateCreateAPIView, RateDetailAPIView, \
                              CommentListAPIView, CommentCreateAPIView, CommentDetailAPIView
                                  
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/rates/', RateListAPIView.as_view(), name='product-rate-list'),
    path('<int:pk>/rate/create/', RateCreateAPIView.as_view(), name='product-rate-create'),
    path('rate/<int:pk>/', RateDetailAPIView.as_view(), name='product-rate-detail'),
    path('<int:pk>/comments/', CommentListAPIView.as_view(), name='product-comment-list'),
    path('<int:pk>/comment/create/', CommentCreateAPIView.as_view(), name='product-comment-create'),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view(), name='product-comment-detail'),
    path('', include(router.urls)),
    path('orderitems/', OrderItemListAPIView.as_view(), name='orderitem-list'),
    path('orderitem/create', OrderItemCreateAPIView.as_view(), name='orderitem-create'),
    path('orderitem/<int:pk>/', OrderItemDetailAPIView.as_view(), name='orderitem-detail'),
    path('orderbox/list/', OrderBoxListAPIView.as_view(), name='orderbox-list'),
    path('orderbox/create/', OrderBoxCreateAPIView.as_view(), name='orderbox-create'),
    path('orderbox/<int:pk>/', OrderBoxDetailAPIView.as_view(), name='orderbox-detail'),
]