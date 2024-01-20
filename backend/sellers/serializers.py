from rest_framework import serializers
from .models import CustomUser, Review
from marketplace.serializers import ProductSerializer



class RegisterUserSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    class Meta:
        model = CustomUser
        fields = ('phone', 'nick', 'first_name', 'second_name', 'last_name',
                  'city', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода и создания отзывов"""
    class Meta:
        model = Review
        fields = '__all__'


#TODO: РАЗБИТЬ
class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для просмтра СВОЕГО профиля"""
    products = ProductSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = ('phone', 'email', 'nick', 'first_name', 'second_name', 'last_name',
        'profile_photo', 'city', 'created_at', 'products', 'reviews')

