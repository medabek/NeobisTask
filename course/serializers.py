from rest_framework import serializers, models, status
from rest_framework.response import Response

from course.models import Course, Category, Branch, Contact

class ContactSerializers(serializers.ModelSerializer):
    contact_choice = serializers.SerializerMethodField()
    # value = serializers.CharField(read_only=True)
    class Meta:
        model = Contact
        fields = ('contact_choice', 'value',)

    def get_contact_choice(self, obj):
        return obj.get_contact_choice_display()





class BranchSerializer(serializers.ModelSerializer):
    # latitude = serializers.ReadOnlyField(read_only=True)
    # longitude = serializers.ReadOnlyField(read_only=True)
    # address = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address',)


class CategorySerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    #imgpath = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Category
        fields = ('name',)


class CourseSerializer(serializers.ModelSerializer):

    contacts = ContactSerializers(many=True, required=False)#serializers.SerializerMethodField()#StringRelatedField( many=True)
    branches = BranchSerializer(many=True, required=False)#serializers.SerializerMethodField("get_branch")
    category = CategorySerializers()
    # category = category(source='name')

    class Meta:
        model = Course
        fields = ("id", "name", "description", "logo", "category", "contacts", "branches")


    #
    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     course = Course.objects.create(**validated_data)
    #     Category.objects.create(category=course, **category_data)
    #     #print(validated_data)
    #     return course #Course.objects.create(validated_data)

    def create(self, validated_data):
        categ_data = validated_data.pop('category')
        cont_data = validated_data.pop('contacts')
        bran_data = validated_data.pop('branches')
        categ_value = categ_data['name']
        course = Course.objects.create(**validated_data, category=Category.objects.get(name=categ_value))
        for contact in cont_data:
            Contact.objects.create(course=course, **contact)
        for branch in bran_data:
            Branch.objects.create(course=course, **branch)
        return course

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     category = Category.objects.get(name=category_data['name'])
    #     course = Course.objects.create(name=validated_data['category'], category=category)
    #  categy object found by it's description
    #     return course


    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        instance.branches = validated_data.get('branches', instance.branches)
        instance.save()
        return instance
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.logo = validated_data.get('logo', instance.logo)
    #     instance.save()
    #
    #     courses = validated_data.get('course')
    #     for cours in courses:
    #         inv_item = Course.objects.get(category=instance, pk=id)
    #         inv_item.name = cours.get('name', inv_item.name)
    #         inv_item.imgpath = cours.get('imgpath', inv_item.imgpath)
    #         inv_item.course = instance
    #         inv_item.save()
    #
    #     contacts = validated_data.get('contacts')
    #     for con in contacts:
    #         inv_item = Contact.objects.get(contacts=instance, pk=id)
    #         inv_item.contact_choice = con.get('contact_choice', inv_item.contact_choice)
    #         inv_item.value = con.get('value', inv_item.value)
    #         inv_item.course = instance
    #         inv_item.save()
    #
    #     branches = validated_data.get('branches')
    #     for bran in branches:
    #         inv_item = Branch.objects.get(branches=instance, pk=id)
    #         inv_item.latitude = bran.get('latitude', inv_item.latitude)
    #         inv_item.longitude = bran.get('longitude', inv_item.longitude)
    #         inv_item.address = bran.get('address', inv_item.address)
    #         inv_item.course = instance
    #         inv_item.save()
    #
    #     instance.save()
    #     return instance



  #
    # @staticmethod
    # def get_contacts(self):
    #     contacts = ContactSerializers(Contact.objects.all(), many=True)
    #     return contacts.data
    #
    # # def get_contact_choice(self, obj):
    # #     return obj.get_contact_choice_display()
    #
    # @staticmethod
    # def get_branch(self):
    #     branches = BranchSerializer(Branch.objects.all(), many=True)
    #     return branches.data
    #
    # @staticmethod
    # def get_category_name(self):
    #     category = CategorySerializers(Category)
    #     return category