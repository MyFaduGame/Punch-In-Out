from django.contrib import admin
from django.urls import path,include

from punchinout.api.v1.views import timeinview,timeoutview,PunchInPage

urlpatterns = [
   path('timein/',timeinview.as_view()),
   path('timein/<int:pk>',timeinview.as_view()),
   path('timeout/',timeoutview.as_view()),
   path('timeout/<int:pk>',timeoutview.as_view()),
   path('index/',PunchInPage, name='indexpage')

]
