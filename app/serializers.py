from rest_framework import serializers
from .models import *

# class StudentSerializer(serializers.ModelSerializer):
   
#     class Meta:
#         model = Student
#         fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    # student = StudentSerializer()
    class Meta:
        model = Classroom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()
    class Meta:
        model = Student
        fields = '__all__'