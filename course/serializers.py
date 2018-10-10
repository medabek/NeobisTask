from rest_framework import serializers, models
from course.models import Course, Category, Branch, Contact

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact_choice', 'value')

class BranchSerializer(serializers.ModelSerializer):
    latitude = serializers.CharField(required=False, allow_blank=True, max_length=300)
    longitude = serializers.CharField(required=False, allow_blank=True, max_length=300)
    address = serializers.CharField(required=False, allow_blank=True, max_length=300)
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class CategorySerializers(serializers.ModelSerializer):
    #name = serializers.CharField(required=False, allow_blank=True, max_length=250)

    class Meta:
        model = Category
        fields = ('name', 'imgpath')

class CourseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1500)
    logo = serializers.CharField(required=False, allow_blank=True, max_length=250)
    category = CategorySerializers(read_only=True)
    #category = serializers.CharField(required=False, allow_blank=True, max_length=250)
    contacts = ContactSerializers(read_only=True)
    branches = BranchSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', "name", "description", "logo", "category", "contacts", "branches")


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        instance.branches = validated_data.get('branches', instance.branches)
        instance.save()
        return instance