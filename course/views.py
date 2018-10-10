from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Course
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from course.models import Course
from course.serializers import CourseSerializer
from rest_framework import generics



def home(request):
    course = Course.objects.all()
    return render(request, 'home.html', {'course': course})




class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



# #@api_view(['GET', 'POST'])
# #def course_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#   #  if request.method == 'GET':
#   #      course = Course.objects.all()
#   #      serializer = CourseSerializer(course, many=True)
#  #       return Response(serializer.data)
# #
#    # elif request.method == 'POST':
#   #      serializer = CourseSerializer(data=request.data)
#  #       if serializer.is_valid():
# #            serializer.save()
# #            return Response(serializer.data, status=status.HTTP_201_CREATED)
# #        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CourseList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def course_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         course = Course.objects.get(pk=pk)
#     except Course.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class CourseDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)