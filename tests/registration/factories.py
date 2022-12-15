import uuid

import factory
from factory.django import DjangoModelFactory
from django.utils import timezone

from apps.registration.models import Student, Registration


class StudentFactory(DjangoModelFactory):
    id = str(uuid.uuid4())
    name = "Ralph"
    id_doc = "fake_doc"
    created_at = timezone.now()

    class Meta:
        model = Student


class RegistrationFactory(DjangoModelFactory):
    registration = factory.SubFactory(StudentFactory)

    class Meta:
        model = Registration
