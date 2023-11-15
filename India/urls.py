from India.views import *
from django.urls import path
app_name='Rohit'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('sheryas/', sheryas,name='sheryas'),
]