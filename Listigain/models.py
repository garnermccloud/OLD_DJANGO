from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, editable=False)
    CATEGORY_TYPES = (
         ('EDU', 'Educational'),
         ('SOC', 'Social'),
         ('PHY', 'Physical'),
         ('PER', 'Personal')
    )
    PRIORITY_TYPES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )
    category = models.CharField(max_length=200,choices=CATEGORY_TYPES)
    content = models.CharField(max_length=200)
    priority = models.IntegerField(choices=PRIORITY_TYPES)
    completed = models.BooleanField()
    skip = models.BooleanField()
    time = models.IntegerField(default=0,null=False)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('skip','time')

