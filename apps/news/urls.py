from .views import NewsContentListAPIView
from django.urls import path

urlpatterns =[
    path("news/", NewsContentListAPIView.as_view())
]