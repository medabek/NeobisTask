from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.TextField(max_length=250)
    imgpath = models.TextField(max_length=1000)


    def __unicode__(self):
        return u"%s" % self.name

class Branch(models.Model):
    latitude = models.TextField(max_length=300)
    longitude = models.TextField(max_length=300)
    address = models.TextField(max_length=300)

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


class Course(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1500)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='items')
    logo = models.TextField(max_length=1000)
    contacts = models.ForeignKey(Contact, on_delete= models.CASCADE,related_name='tracks')
    branches = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.description, self.logo, self.category

    class Meta:
        unique_together = ('name', 'category')



