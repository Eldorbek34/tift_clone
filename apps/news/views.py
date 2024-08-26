from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.utils import timezone
from .models import NewsContent  # NewsContent modelini import qilyapsiz
from .serializers import NewsContentSerializer  # Serializerni import qilyapsiz

class NewsContentListAPIView(ListAPIView):
    queryset = NewsContent.objects.filter(
        is_published=True, 
        publish_time__lte=timezone.now()
    )
    serializer_class = NewsContentSerializer
