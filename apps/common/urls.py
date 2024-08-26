from django.urls import path
from .views import (
    RegionListAPIView,
    RegionDetailAPIView,
    DistrictListAPIView,
    DistrictDetailAPIView,
    SocialListAPIView,
    SocialDetailAPIView
)

urlpatterns = [
    path('regions/', RegionListAPIView.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionDetailAPIView.as_view(), name='region-detail'),
    path('districts/', DistrictListAPIView.as_view(), name='district-list'),
    path('districts/<int:pk>/', DistrictDetailAPIView.as_view(), name='district-detail'),
    path('socials/', SocialListAPIView.as_view(), name='social-list'),
    path('socials/<int:pk>/', SocialDetailAPIView.as_view(), name='social-detail'),
]
