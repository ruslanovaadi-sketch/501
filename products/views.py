from rest_framework.decorators import api_view
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.generics import status, ListAPIView,generics
from .models import Product, Category, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer
)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            rating=Avg('reviews__stars')
        ).prefetch_related('reviews')


class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
