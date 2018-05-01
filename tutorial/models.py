from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PythonTutorial(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'),
                     ('published', 'Published'),
                     )
    tuts_tag = models.CharField(max_length=250, default="Python")
    questionTitle = models.CharField(max_length=250)
    questionSlug = models.CharField(max_length=250)
    py_solution_body = models.TextField(default="add something")
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')


class GolangTutorial(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'),
                     ('published', 'Published'),
                     )
    tuts_tag = models.CharField(max_length=250, default="Golang")
    questionTitle = models.CharField(max_length=250)
    questionSlug = models.CharField(max_length=250)
    go_solution_body = models.TextField(default="add something")
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')


class ProjectEularSolution(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'),
                     ('published', 'Published'),
                     )
    tuts_tag = models.CharField(max_length=250, default="ProjectEular")
    questionTitle = models.CharField(max_length=250)
    questionSlug = models.CharField(max_length=250)
    pe_solution_body = models.TextField(default="add some")
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')


