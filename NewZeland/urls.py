from NewZeland.views import *
from django.urls import path
app_name='Phillips'
urlpatterns=[
    path('williamson/',williamson,name='williamson'),
    path('boult/',boult,name='boult'),

]