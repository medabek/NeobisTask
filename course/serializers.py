from rest_framework import serializers, models
from course.models import Course, Category, Branch, Contact

class ContactSerializers(serializers.ModelSerializer):
    contact_choice = serializers.CharField(read_only=True)
    value = serializers.CharField(read_only=True)
    class Meta:
        model = Contact
        fields = ('contact_choice', 'value',)





class BranchSerializer(serializers.ModelSerializer):
    latitude = serializers.ReadOnlyField(read_only=True)
    longitude = serializers.ReadOnlyField(read_only=True)
    address = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address',)



class CategorySerializers(serializers.ModelSerializer):
    # name = serializers.CharField(required=False, allow_blank=True, max_length=250)
    name = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Category
        fields = ('name',)

class CourseSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source="category.name")


    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    description = serializers.CharField(required=False, allow_blank=True, max_length=1500)
    logo = serializers.CharField(required=False, allow_blank=True, max_length=250)
    #category = CategorySerializers(Category, required=False)
    contacts = serializers.SerializerMethodField("get_contact")#StringRelatedField( many=True)
    branches = serializers.SerializerMethodField("get_branch")

    class Meta:
        model = Course
        fields = ('id', "name", "description", "logo", "category", "contacts", "branches")


    @staticmethod
    def get_contact(self):
        contacts = ContactSerializers(Contact.objects.all(), many=True, read_only=True, required=False,)
        return contacts.data

    # def get_contact_choice(self, obj):
    #     return obj.get_contact_choice_display()

    @staticmethod
    def get_branch(self):
        branches = BranchSerializer(Branch.objects.all(), many=True, required=False,)
        return branches.data

    @staticmethod
    def get_category_name(self):
        category = CategorySerializers(Category)
        return category

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