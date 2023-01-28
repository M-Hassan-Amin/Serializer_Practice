from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from faker import Faker
from rest_framework.pagination import LimitOffsetPagination
from django.core.paginator import Paginator
from json import dumps
from django.http import HttpResponse

from rest_framework.pagination import PageNumberPagination

fake = Faker()
class AllStudents(APIView):
 
    def get(self, request):
        students = Student.objects.all()
        # students = Student.objects.filter(classroom__classroom = 1) # get data with class room wise....................................................
        serializer = StudentSerializer(students, many=True).data
        return Response({"status": "success", "data": serializer}, status=200)

    def post(self, request):
        # Without Serializer Methods............................................................................................................
        # for i in range(1000):
        #     person = Student(name=fake.name(), gender=fake.random_element(GENDER), location=fake.city(), 
        #             stack= fake.random_element(TYPES), classroom=fake.random_element(Classroom.objects.all()), 
        #             joined_on=fake.date_between(start_date='-30d', end_date='today'))
        #     person.save()
        # return Response({"status": "success", "data": "Done"}, status=200)
        
        # With Serializer Methods............................................................................................................
        
        for i in range(1000):
            data = {'name': fake.name(), 'location': fake.city(),'gender':fake.random_element(['Male','Female','Other']),
                    'joined_on':fake.date_between(start_date='-30d', end_date='today'), 'stack':fake.random_element(['Python','Java']),
                    'classroom':fake.random_element([1,2,3])}
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

        return Response({"status": "success", "Data": 'Done'}, status=200)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
class MyPagination(PageNumberPagination):
    page_size = 25

class page(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        paginator = MyPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
