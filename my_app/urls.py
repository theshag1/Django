from my_app.views import *
from django.urls import path

urlpatterns = [
    path('', requst_1, name='home'),
    path('question/', question_list, name='question'),
    path('question/<int:pk>/', question_detil, name='question_detil'),

]
