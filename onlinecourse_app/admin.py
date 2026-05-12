from django.contrib import admin
from .models import *

admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)