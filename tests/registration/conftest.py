import pytest

from .factories import StudentFactory, RegistrationFactory


@pytest.fixture()
def student():
    return StudentFactory()


@pytest.fixture()
def registration():
    return RegistrationFactory()


@pytest.fixture()
def student_payload():
    return {
        "id": "5456ce9d-8a91-430d-8a01-db0ed614077e",
        "name": "Some name",
        "id_doc": "99999999999",
        "created_at": "2022-12-13T12:49:05-03:00",
    }


@pytest.fixture()
def registration_payload():
    return {
        "id": 1,
        "email": "some_name@test.com",
        "phone": "+5511999999999",
        "gender": "male",
        "degree": "other",
        "contact_name": "Some contact name",
        "contact_number": "+5511999999999",
        "relationship": "mother",
        "student": "5456ce9d-8a91-430d-8a01-db0ed614077e",
    }
