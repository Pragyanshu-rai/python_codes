from django.db import models

# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    branch = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    year = models.CharField(max_length=5)
    
    def __str__(self):
        return "ID: "+str(self.id)+", Name: "+self.name+", Roll: "+str(self.roll)+", Branch: "+self.branch+", Section: "+self.section+", Year: "+self.year
    

