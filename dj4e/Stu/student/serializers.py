from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    branch = serializers.CharField(max_length=10)
    section = serializers.CharField(max_length=10)
    year = serializers.CharField(max_length=5)
    
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        print("Befor:-", instance.branch)        
        instance.branch = validated_data.get("branch", instance.branch)
        print("After:-", instance.branch)
        instance.section = validated_data.get("section", instance.section)
        instance.year = validated_data.get("year", instance.year)
        instance.save()
        return instance
