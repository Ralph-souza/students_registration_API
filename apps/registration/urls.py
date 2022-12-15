from django.urls import path
from . import api

urlpatterns = [
    path("students/", api.student_api_overview, name="home"),
    path("create-student/", api.create_student, name="create-student"),
    path("student-by-id/<str:pk>/", api.get_student_by_id, name="student_by_id-"),
    path("list-students/", api.list_students, name="list-students"),
    path("student/<str:pk>/update/", api.update_student, name="update-student"),
    path("student/<str:pk>/delete/", api.delete_student, name="delete-student"),
    # path("registers/", api.registration_api_overview, name="home"),
    # path("create-register/", api.create_register, name="create-register")
]
