from .views import *
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('AllStudents', AllStudents.as_view()),
    path('page', page.as_view()),
    path('custompage', custompage.as_view()),
    path('register/',UserRegistration.as_view()),
    # path('accountregister/',AccountRegistration.as_view()),
    path('AccountView/',AccountView.as_view()),
    path('userregister/',RegisterView.as_view()),

    
]