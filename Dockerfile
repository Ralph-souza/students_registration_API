FROM python:3.9

COPY . /students_registration_API
WORKDIR /students_registration_API
RUN pip install -r requirements.txt
RUN python manage.py migrate
