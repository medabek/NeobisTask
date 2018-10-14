from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from course import views

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('courses',views.CourseView)
router.register('contacts', views.ContactView)
router.register('branches', views.BranchView)
router.register('category', views.CategoryView)
urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)