from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Region, District, Social
from .serializers import RegionSerializer, DistrictSerializer, SocialSerializer

class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailAPIView(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictDetailAPIView(RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class SocialListAPIView(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class SocialDetailAPIView(RetrieveAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
