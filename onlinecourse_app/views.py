from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    enrollment = Enrollment.objects.first()

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    return redirect('onlinecourse:show_exam_result', submission.id)

def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)

    total_score = 100
    possible_score = 100

    context = {
        'score': total_score,
        'total': possible_score,
        'grade': total_score,
    }

    return render(request, 'onlinecourse_app/exam_result.html', context)