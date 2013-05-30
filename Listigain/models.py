import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# Each task has a user, a series of fields, a start time array, and an end time array


class Task(models.Model):

    CATEGORY_TYPES = (
         ('SCH', 'School'),
         ('MIS', 'Miscellaneous')
    )
    # Level of importance of task (1 = not important at all (optional) ... 7 = Extremely important (required))
    IMPORTANCE_TYPES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7')
        )
    # Level of enjoyment of task (1 = hate working on task ... 7 = love working on task)
    ENJOYMENT_TYPES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7')
        )
    PERCENT_CHOICES = zip( range(0,101), range(0,101) )

    # User inputted fields
    category = models.CharField(max_length=3,choices=CATEGORY_TYPES)
    content = models.CharField(max_length=100)
    date_due = models.DateTimeField(default=datetime.datetime.today())
    duration_est = models.IntegerField(default=0,null=False, max_length=4)
    importance = models.IntegerField(max_length=1,choices=IMPORTANCE_TYPES, default=4)
    enjoyment = models.IntegerField(max_length=1,choices=ENJOYMENT_TYPES, default=4)
    complete_percentage = models.IntegerField(default=0,null=False, max_length=4, choices=PERCENT_CHOICES)
    completed = models.BooleanField()

    # Automatically inputted fields
    user = models.ForeignKey(User, editable=False)
    time_created = models.DateTimeField(default=datetime.datetime.today(), null=True)




# An array of DateTimes where the user has started working on the task
class Start_Time(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField(default=datetime.datetime.today())

# An array of DateTimes where the user has finished working on the task
class End_Time(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField(default=datetime.datetime.today())

    # An array of DateTimes where the user has started working on the task
class Marginal_Duration(models.Model):
    task = models.ForeignKey(Task)
    marginal_duration = models.FloatField(default=0)
    time = models.DateTimeField(default=datetime.datetime.today())



class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('time_created')



