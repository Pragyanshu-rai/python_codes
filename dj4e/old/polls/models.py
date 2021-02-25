import datetime

from django.db import models

from django.utils import timezone
# Create your models here.

class Question(models.Model): # table name
    question_text = models.CharField(max_length=200) #table columns(feilds)
    pub_date = models.DateTimeField('date published') # same
    def __str__(this):
        return this.question_text
    def was_published_recently(this):
        return this.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(this):
        return this.choice_text


