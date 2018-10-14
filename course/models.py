from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    imgpath = models.CharField(max_length=1000)

    def __unicode__(self):
        return u"%s" % self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    logo = models.CharField(max_length=1000)

    #
    # def __str__(self):
    #     return self.name, self.description, self.logo, self.category

    def __str__(self):
        template = '{0.name} {0.description} {0.logo}'
        return template.format(self)

    # class Meta:
    #     unique_together = ('name', 'category')


class Branch(models.Model):
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    branches = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.name

class Contact(models.Model):
    contact_choice=(
        (1, "PHONE"),
        (2, "FACEBOOK"),
        (3, "EMAIL"),
    )

    contact_choice = models.IntegerField(choices=contact_choice)
    value = models.CharField(max_length=200)
    contacts = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
    class Meta:
        unique_together = ('contact_choice', 'value')

    def __unicode__(self):
        return '%d: %s' % (self.contact_choice, self.value)




