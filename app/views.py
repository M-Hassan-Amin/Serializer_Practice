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
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes


fake = Faker()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# start = (page_number - 1) * 25
#         end = start + 25
#         records = Student.objects.all()[start:end]
#         serializer = StudentSerializer(records, many=True).data

# With Serializer Methods..
class MyPagination(PageNumberPagination):
    page_size = 100

class page(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        paginator = MyPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Custom Pagination With Serializer Methods..

class custompage(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    print("authentication_classes",authentication_classes)
    print("permission_classes",permission_classes)
    def get(self, request):
        page_number = int(request.GET.get('page'))
        start = (page_number - 1) * 25
        end = start + 25
        records = Student.objects.all()[start:end]
        print(len(records))
        serializer = StudentSerializer(records, many=True).data
        return Response({'Next Page' : page_number+1, 'Previous Page' : page_number-1,"status": "success", 
                        'records': serializer, 'Next Page' : page_number+1, 'Previous Page' : page_number-1}, status=200)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class UserRegistration(APIView):

    def post(self,request):

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        # token_obj , _ = Token.objects.get_or_create(user=user)

        ################ for jwt ###################################
        refresh = RefreshToken.for_user(user)

        # return Response({'status':200,'data':serializer.data,'token_obj':str(token_obj),'message':'your data is saved'})

        return Response({'status':200,
        'data':serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'message':'your data is saved'})




# class AccountRegistration(APIView):

#     def post(self,request):

#         serializer = AccountSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

#         serializer.save()
#         user = Accounts.objects.get(name = serializer.data['name'])
#         # token_obj , _ = Token.objects.get_or_create(user=user)

#         ################ for jwt ###################################
#         refresh = RefreshToken.for_user(user)

#         # return Response({'status':200,'data':serializer.data,'token_obj':str(token_obj),'message':'your data is saved'})

#         return Response({'status':200,
#         'data':serializer.data,
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#         'message':'your data is saved'})

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

class AccountView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer

    def get_object(self):
        MyAccount.objects.create(username='user1', password='pass1')
        refresh = RefreshToken.for_user(MyAccount.objects.get(username='user1'))
        access_token = refresh.access_token

        return self.request.user

