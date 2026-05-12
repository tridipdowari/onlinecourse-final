from django.shortcuts import render
from django.http import HttpResponse

def course_detail(request):
    return render(request, 'onlinecourse_app/course_details_bootstrap.html')

def submit(request):
    return HttpResponse("Exam Submitted")

def show_exam_result(request):
    return HttpResponse("Congratulations! Your score is 100%")