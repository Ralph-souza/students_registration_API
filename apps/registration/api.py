from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import Student, Registration
from .serializers import StudentSerializer, RegistrationSerializer


class StudentViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    queryset = Student.objects.all().order_by("created_at")
    serializer_class = StudentSerializer


class RegistrationViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "update", "patch", "delete"]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
