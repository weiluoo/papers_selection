from django.db import models
from django.contrib.auth.models import User

import datetime


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a subject (e.g. CNN, RNN, GAN etc.)')

    def __str__(self):
        return self.name


class Paper(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a brief name of the paper')
    title = models.CharField(max_length=255, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, help_text='Select a subject for this paper')
    author = models.CharField(max_length=100)

    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]

    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.date.today().year, help_text='Enter the year when it published')
    link = models.URLField()
    presenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    available = models.BooleanField(default=True, help_text='Is the paper chosen or not')

    def __str__(self):
        return self.name

    def display_subject(self):
        return self.subject.name
