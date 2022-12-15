import pytest
from rest_framework.test import RequestsClient
from rest_framework import status

from apps.registration.models import Student, Registration
from .factories import StudentFactory

pytestmark = pytest.mark.django_db


class TestStudentViewSet:
    def test_create_student(self, student_payload):
        rc = RequestsClient()
        request = rc.post("http://127.0.0.1:8000/v1/api/student/", student_payload)

        assert request.status_code == status.HTTP_201_CREATED
        assert Student.objects.count() == 1

    def test_create_student_fail(self, student_payload_invalid):
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/student/", student_payload_invalid
        )

        assert request.status_code == status.HTTP_400_BAD_REQUEST
        assert Student.objects.count() == 0

    def test_update_student(self):
        student = StudentFactory()
        rc = RequestsClient()
        request = rc.put(
            f"http://127.0.0.1:8000/v1/api/student/{student.id}/",
            {"name": "fake_name", "id_doc": "fake_doc"},
        )
        response_data = eval(request.content)

        assert request.status_code == status.HTTP_200_OK
        assert response_data["name"] == "fake_name"

    def test_list_students(self):
        rc = RequestsClient()
        request = rc.get("http://127.0.0.1:8000/v1/api/student/")

        assert request.status_code == status.HTTP_200_OK

    def test_get_student_by_id(self):
        student = StudentFactory()
        rc = RequestsClient()
        request = rc.get(f"http://127.0.0.1:8000/v1/api/student/{student.id}/")

        assert request.status_code == status.HTTP_200_OK

    def test_delete_student(self, student_payload):
        rc = RequestsClient()
        request = rc.post("http://127.0.0.1:8000/v1/api/student/", student_payload)
        response_data = eval(request.content)
        r_exclude = rc.delete(
            f"http://127.0.0.1:8000/v1/api/student/{response_data['id']}"
        )

        assert r_exclude.status_code == status.HTTP_204_NO_CONTENT
        assert Student.objects.count() == 0


class TestRegistrationViewSet:
    def test_create_registration(self):
        student = StudentFactory()
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/registration/",
            {
                "email": "some_name@test.com",
                "phone": "+5511999999999",
                "gender": "male",
                "degree": "other",
                "contact_name": "Some contact name",
                "contact_number": "+5511999999999",
                "relationship": "mother",
                "student": student.id,
            },
        )

        assert request.status_code == status.HTTP_201_CREATED
        assert Registration.objects.count() == 1

    def test_create_registration_fail(self):
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/registration/",
            {
                "email": "some_name@test.com",
                "phone": "+5511999999999",
                "gender": "male",
                "degree": "other",
                "contact_name": "Some contact name",
                "contact_number": "+5511999999999",
                "relationship": "mother",
                "student": None,
            },
        )

        assert request.status_code == status.HTTP_400_BAD_REQUEST
        assert Registration.objects.count() == 0

    def test_update_registration(self):
        student = StudentFactory()
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/registration/",
            {
                "email": "some_name@test.com",
                "phone": "+5511999999999",
                "gender": "male",
                "degree": "other",
                "contact_name": "Some contact name",
                "contact_number": "+5511999999999",
                "relationship": "mother",
                "student": student.id,
            },
        )
        response_data = eval(request.content)

        update = rc.put(
            f"http://127.0.0.1:8000/v1/api/registration/{response_data['id']}/",
            {
                "email": "some_new_name@test.com",
                "phone": "+5511333333333",
                "student": response_data["student"],
            },
        )

        assert update.status_code == status.HTTP_200_OK

    def test_list_registrations(self):
        rc = RequestsClient()
        request = rc.get("http://127.0.0.1:8000/v1/api/registration/")

        assert request.status_code == status.HTTP_200_OK

    def test_get_registration_by_id(self):
        student = StudentFactory()
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/registration/",
            {
                "email": "some_name@test.com",
                "phone": "+5511999999999",
                "gender": "male",
                "degree": "other",
                "contact_name": "Some contact name",
                "contact_number": "+5511999999999",
                "relationship": "mother",
                "student": student.id,
            },
        )
        response_data = eval(request.content)
        registration_by_id = rc.get(
            f"http://127.0.0.1:8000/v1/api/registration/{response_data['id']}/"
        )

        assert registration_by_id.status_code == status.HTTP_200_OK

    def test_delete_student(self, student_payload):
        student = StudentFactory()
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/registration/",
            {
                "email": "some_name@test.com",
                "phone": "+5511999999999",
                "gender": "male",
                "degree": "other",
                "contact_name": "Some contact name",
                "contact_number": "+5511999999999",
                "relationship": "mother",
                "student": student.id,
            },
        )
        response_data = eval(request.content)
        r_exclude = rc.delete(
            f"http://127.0.0.1:8000/v1/api/registration/{response_data['id']}/"
        )

        assert r_exclude.status_code == status.HTTP_204_NO_CONTENT
        assert Registration.objects.count() == 0
