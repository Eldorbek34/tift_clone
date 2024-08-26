from rest_framework import serializers
from .models import NewsContent

class NewsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ("title", "body", "slug", "publish_time",)