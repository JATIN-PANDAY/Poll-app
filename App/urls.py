from django.contrib import admin
from django.urls import path,include
from App import views
urlpatterns = [
    path('', views.index,name='index'),
    path('createquestion',views.createquestion,name='createquestion'),
    path('vote/<poll_id>',views.vote,name='vote'),
    path('result/<poll_id>',views.result,name='result'),

    





]
