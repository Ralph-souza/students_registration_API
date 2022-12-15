import uuid

import factory
from factory.django import DjangoModelFactory

from apps.registration.models import Student, Registration


class StudentFactory(DjangoModelFactory):
    id = str(uuid.uuid4())

    class Meta:
        model = Student


class RegistrationFactory(DjangoModelFactory):
    registration = factory.SubFactory(StudentFactory)

    class Meta:
        model = Registration
