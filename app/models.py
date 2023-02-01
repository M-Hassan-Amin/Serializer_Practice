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

class Accounts(models.Model):
    name = models.CharField(max_length=55)
    designation = models.CharField(max_length=55)
    email = models.EmailField(unique = True)
    password = models.TextField()

class MyAccount(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings
from decouple import config

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=255,null=True,blank=True)
    email_verification_token = models.CharField(max_length=200,null=True,blank=True)
    forget_password_token = models.CharField(max_length=200,null=True,blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def name(self):
        return self.first_name + ' ' + self.last_name

    def _str_(self):
        return self.email 

import uuid
@receiver(post_save,sender=User)
def send_email_token(sender,instance,created,**kwargs):
    if created:
        print("run------------")
        try:
            subject = "You email needs to be verified"
            message = f'Hi ,click on the link to verify email http://127.0.0.1:8000/{uuid.uuid4()}/'
            email_from = config('EMAIL_HOST_USER')
            receipent_list = [instance.email]
            send_mail(subject,message,email_from,receipent_list)


        except Exception as e:
            print(e)