from django.urls import path
from .views import( ProductReviewListAPIview,ProductListAPIView,CategoryDetailAPIView,CategoryListAPIView,ProductDetailAPIView,ReviewDetailAPIView,ReviewListAPIView,CategoryCreateView,CategoryDetailView,ProductCreateView,ProductDetailView,ReviewCreateView,ReviewDetailView)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:id>/', ProductDetailAPIView.as_view()),

    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view()),
    path('products/reviews',
         ProductReviewListAPIview.as_view(),
         name='products-reviews'
    ), # categories  
    path('categories/', CategoryCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    # products
    path('products/', ProductCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),

    # reviews
    path('reviews/', ReviewCreateView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailView.as_view()),
  

] 