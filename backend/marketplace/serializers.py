from rest_framework import serializers
from .models import *
from sellers.models import CustomUser
from sellers.serializers import ReviewSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'alt_text']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'image']


class ProductListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка товаров"""
    images = ImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'discount_price', 'subcategory', 'images', 'colors', 'seller']


class ProductRetrieveSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра конкретного товара"""
    images = ImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'subcategory', 'style', 'city', 'name',
                  'price', 'discount_price', 'quantity', 'description', 'likes',
                  'condition', 'posted_at', 'uid', 'slug', 'gender', 'images', 'colors', 'seller']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['name', 'slug', 'description']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'slug']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'slug']


class SellerSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра профиля продавца"""
    products = ProductListSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['nick', 'profile_photo', 'city', 'created_at', 'products', 'reviews']

