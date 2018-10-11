from django.contrib import admin
from .models import Contact, Course, Branch, Category
#from .serializers import CategorySerializers
# Register your models here.
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Category)
