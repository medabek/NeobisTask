from django.apps import AppConfig
from gevent.pywsgi import WSGIServer


class CourseConfig(AppConfig):
    name = 'course'
