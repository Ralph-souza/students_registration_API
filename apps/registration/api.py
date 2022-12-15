from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def student_api_overview(request):
    api_urls = {
        "All-students": "/students",
        "Search by Student": "/student_by_id",
        "Create": "/create",
        "Update": "/update/pk",
        "Delete": "/student/pk/delete",
    }
    return Response(api_urls)


@api_view(["POST"])
def create_student(request):
    student = StudentSerializer(data=request.data)
    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data already exists")

    if student.is_valid():
        student.save()
        return Response(student.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def list_students(request):
    if request.query_params:
        students = Student.objects.filter(**request.query_param.dict())
    else:
        students = Student.objects.all()

    if students:
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_student_by_id(request, pk):
    student = Student.objects.get(pk=pk)

    if student:
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
