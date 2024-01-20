from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser, Review
from marketplace.models import Product
from marketplace.serializers import ProductSerializer


class RegisterUserAPIView(APIView):
    """Вью для регистрации аккаунта"""
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Вью для просмотра, редактирования и удаления своего профиля"""
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'nick'
    permission_classes = [permissions.IsAuthenticated]


class CreateProductAPIView(generics.CreateAPIView):
    """Вью для создания обьявления"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class CreateReviewAPIView(generics.CreateAPIView):
    """Вью для создания отзыва"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
