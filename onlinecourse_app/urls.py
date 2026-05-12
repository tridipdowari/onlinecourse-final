from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_detail, name='course_detail'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.show_exam_result, name='result'),
]