from statistics import mode
import uuid
from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.utils import timezone

GENDER = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Other','OTHER'),
)
 
TYPES =(    
    ('Python', 'PYTHON'),
    ('Java', 'JAVA'),
)


class Classroom(models.Model):
    # student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE, related_name='student_details')
    classroom = models.CharField(blank=True, null=True, max_length=85)
    mentor = models.CharField(blank=True, null=True, max_length=85)
    joined_on = models.DateTimeField(default=timezone.now)

class Student(models.Model):
    name = models.CharField(max_length=55, default='')
    gender = models.CharField(choices=GENDER, max_length=55, default='')
    location = models.CharField(max_length=55, default='')
    stack = models.CharField(choices=TYPES, max_length=55, default='')
    classroom = models.ForeignKey(Classroom, blank=True, null=True, on_delete=models.CASCADE, related_name='student_details')
    joined_on = models.DateField(default=timezone.now)

