from rest_framework import serializers
from .models import *


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # classroom = ClassroomSerializer()
    class Meta:
        model = Student
        fields = '__all__' #['name', 'location','gender', 'joined_on', 'stack', 'classroom']
