from django.urls import path
from .views import *

app_name = 'seller'

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='user_registration'),
    path('profile/<str:nick>', ProfileAPIView.as_view(), name='user_profile'),
    path('profile/<str:nick>/create', CreateProductAPIView.as_view(), name='create_product'),
    path('review/create/', CreateReviewAPIView.as_view(), name='create_review')
]
