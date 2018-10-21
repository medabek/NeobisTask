
from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Course, Category


class CourseModelTest(TestCase):

    def test_string_representation(self):
        course = Course(name="My entry title", description="it is a my live")
        self.assertEqual(str(course), course.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Course._meta.verbose_name_plural), "courses")

    def test_course_name_label(self):
        course = Course.objects.filter(id=1)
        name = course.__str__()
        self.assertEquals(name, 'java')

# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#

# Create your tests here.
