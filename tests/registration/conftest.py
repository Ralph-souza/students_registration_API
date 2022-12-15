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
    return {"id_doc": "some_doc_id", "name": "some_name"}


@pytest.fixture()
def student_payload_invalid():
    return {"id_doc": None, "name": "some_name"}


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
        "student": id,
    }
