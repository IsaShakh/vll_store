from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

app_name = 'marketplace'

urlpatterns = [
    # path("products/",ProductListAPIView.as_view() , name="product_list"),
    # path("products/<slug:slug>/",ProductDetailAPIView.as_view() , name="product_detail"),
    path('products/', ProductViewSet.as_view({'get':'list'})),
    path('products/<slug:slug>/', ProductViewSet.as_view({'get':'retrieve'})),
    path("categories/",CategoryListAPIView.as_view() , name="category_list"),
    path("categories/<str:category_slug>",CategoryItemsAPIView.as_view() , name="category_items"),
    path("subcategories/",SubcategoryListAPIView.as_view() , name="subcategory_list"),
    path("subcategories/<str:subcategory_slug>",SubcategoryItemsAPIView.as_view() , name="subcategory_items"),
    path("styles/",StyleListAPIView.as_view() , name="style_list"),
    path("styles/<str:style_slug>",StyleItemsAPIView.as_view() , name="style_items"),
    path('seller/<str:nick>/', SellerRetrieveAPIView.as_view(), name="seller_profile")

]
