from django.urls import path
from .views import FacultyListAPIView

urlpatterns = [
    path("faculties", FacultyListAPIView.as_view())
]