from rest_framework import serializers
from .models import Region, District, Social

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title', 'order_id']

class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = District
        fields = ['id', 'title', 'region', 'order_id']

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'title', 'social', 'link']
