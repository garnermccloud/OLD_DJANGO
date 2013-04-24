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
        ('1','1 (Not urgent)'),
        ('2','2 (Need to do sooner than later)'),
        ('3','3 (Get this done soon)'),
        ('4','4 (Need to do this ASAP)'),
        ('5','5 (OMG WTF, DO THIS NOW!!!!!)')
    )
    DIFFICULTY_TYPES = (
        ('1','1 (Piece of cake)'),
        ('2',"2 (This isn't so bad)"),
        ('3','3 (Could be better, could be worse)'),
        ('4','4 (Definitely a headache)'),
        ('5','5 (May as well climb Everest)')
    )

    category = models.CharField(max_length=3,choices=CATEGORY_TYPES)
    content = models.CharField(max_length=200)
    priority = models.CharField(max_length=3,choices=PRIORITY_TYPES)
    difficulty = models.CharField(max_length=3,choices=DIFFICULTY_TYPES)
    completed = models.BooleanField()
    skip = models.BooleanField()
    time = models.IntegerField(default=0,null=False)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('skip','time')

