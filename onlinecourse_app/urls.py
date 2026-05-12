from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_detail, name='course_detail'),
    path('int:course_id/submit/', views.submit, name='submit'),
    path('exam/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]