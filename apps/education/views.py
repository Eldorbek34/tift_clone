from rest_framework.generics import ListAPIView
from .models import Faculty
from .serializer import FacultyListSerializer

class FacultyListAPIView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyListSerializer
