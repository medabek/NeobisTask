
from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Course, Category, Contact, Branch


class CourseModelTest(TestCase):


    def test_string_representation(self):
        cat = Category('sci', 'loh')

        cont = Contact()
        cont.contact_choice = "PHONE"
        cont.value = "5555"

       # br = Branch('e32424','2343242','iaau.edu.kg')

        course = Course(name="My entry title", description="it is a my live", logo="lj.kg", category=cat)
        self.assertEqual(str(course), course.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Course._meta.verbose_name_plural), "courses")
    #
    # def test_course_name_label(self ):
    #     course_id = 1
    #     course = Course.objects.get(id=course_id)
    #     name = str(course)
    #     self.assertEquals(name, 'java')

# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#

# Create your tests here.
