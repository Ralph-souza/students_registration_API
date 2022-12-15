from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework import serializers

from .models import Student, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class RegistrationSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"
