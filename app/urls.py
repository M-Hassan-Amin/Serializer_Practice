from .views import *
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('AllStudents', AllStudents.as_view()),
    
]