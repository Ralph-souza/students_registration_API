import pytest

from apps.registration.serializers import StudentSerializer

pytestmark = pytest.mark.django_db


class TestStudentSerializer:
    def test_serializer_read_only_fields(self, student_payload):
        student_payload["id"] == "5456ce9d-8a91-430d-8a01-db0ed614077e"
        student_payload["created_at"] == "2022-12-13T12:49:05-03:00"
        serializer = StudentSerializer(data=student_payload)

        assert serializer.is_valid() is True
        assert "id" not in serializer.validated_data
        assert "created_at" not in serializer.validated_data
