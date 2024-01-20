from . import models
from .serializers import *
from .models import Product, Category
from sellers.models import CustomUser
from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.permissions import AllowAny


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [AllowAny]


# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'
#     permission_classes = [AllowAny]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Вью для вывода списка продуктов и отдельного продукта"""
    queryset = Product.objects.all()
    lookup_field = 'slug'
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductRetrieveSerializer


class CategoryListAPIView(generics.ListAPIView):
    """Вью для вывода названий категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryItemsAPIView(generics.ListAPIView):
    """Вью для вывода товаров принадлежащих конкретной категории"""
    serializer_class = ProductListSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        return Product.objects.filter(category__slug=category_slug)


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryItemsAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        subcategory_slug = self.kwargs.get('subcategory_slug')
        return Product.objects.filter(subcategory__slug=subcategory_slug)


class StyleListAPIView(generics.ListAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class StyleItemsAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        style_slug = self.kwargs.get('style_slug')
        return Product.objects.filter(style__slug=style_slug)


class SellerRetrieveAPIView(generics.RetrieveAPIView):
    """Вью для просмотра профиля продавца"""
    serializer_class = SellerSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'nick'
    permission_classes = [permissions.AllowAny]
