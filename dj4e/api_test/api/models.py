from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    roll = models.IntegerField(unique=True)
    branch = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    year = models.CharField(max_length=5)

    def __str__(self):

        return "ID: "+str(self.id)+", Name: "+self.user.username+", Roll: "+str(self.roll)+", Branch: "+self.branch+", Section: "+self.section+", Year: "+self.year


class Course(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=10, default=None)
    c_code = models.CharField(max_length=10, default=None)

    def __str__(self):

        return "ID: "+str(self.id)+", Student: "+str(self.student.user.username)+", c_name: "+self.c_name+", c_code: "+self.c_code

    def get_dict(self):

        return {"ID":str(self.id), "Student":str(self.student.user.username), "c_name":self.c_name, "c_code":self.c_code}