from rest_framework import fields, serializers
from .models import Student, Course
from django.contrib.auth.models import User
from .APIUtils import userUpdate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = []
        # fields = "__all__"
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email"
        ]


class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Student
        fields = "__all__"
        derpth = 1

    def create(self, validated_data):
        print(validated_data)
        items = validated_data.pop('user')
        print(items)
        try:
            x = items.pop("password")
            user = User.objects.create(**items)
            user.set_password(x)
            user.save()
            print(validated_data)
            student = Student.objects.create(user=user, **validated_data)
        except Exception as ex:
            print("Exception:", ex)
            return ex
        return student

    def update(self, instance, validated_data):

        print("In-Update")
        print(validated_data)
        items = validated_data.pop("user")

        # user = User.objects.get(id = validated_data.pop("user_id"))
        user = instance.user
        print(items, "\n", user)
        user = userUpdate(user, items)

        print(validated_data)
        instance.user = user
        instance.gender = validated_data.get("gender", instance.gender)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.branch = validated_data.get("branch", instance.branch)
        instance.section = validated_data.get("section", instance.section)
        instance.year = validated_data.get("year", instance.year)
        instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):

    student = StudentSerializer()

    class Meta:
        model = Course
        fields = [
            "id",
            "c_code",
            "c_name",
            "student"
        ]
