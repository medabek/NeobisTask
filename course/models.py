from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    imgpath = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'categories'




class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    category = models.ForeignKey(Category, related_name='courses', null=True, on_delete=models.CASCADE)
    logo = models.CharField(max_length=1000)

    #
    # def __str__(self):
    #     return self.name, self.description, self.logo, self.category

    def __str__(self):

        return self.name

    # class Meta:
    #     unique_together = ('name', 'category')


class Branch(models.Model):
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    course = models.ForeignKey(Course, related_name='branches', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'branches'


class Contact(models.Model):
    contact_choice=(
        (1, "PHONE"),
        (2, "FACEBOOK"),
        (3, "EMAIL"),
    )

    contact_choice = models.IntegerField(choices=contact_choice, default=1)
    value = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='contacts')





