from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import bcrypt

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']

    def create(self,validated_data):
        
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


       


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        
        fields = ['name','password','designation','email']

    def create(self,validated_data):
        
        # user.make_password(validated_data['password'])
        password = validated_data.pop('password')
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # validated_data['password'] = password
        user = Accounts.objects.create(name = validated_data['name'],designation = validated_data['designation'],email = validated_data['email'],password=password)
        user.save()
        return user



class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # classroom = ClassroomSerializer()
    class Meta:
        model = Student
        fields = '__all__' #['name', 'location','gender', 'joined_on', 'stack', 'classroom']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAccount
        fields = ('username', 'password')


class CustomeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','password','phone']

    def create(self,validated_data):
        
        user = User.objects.create(email = validated_data['email'],phone = validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        # send_otp_mobile(user.phone,user)
        return user