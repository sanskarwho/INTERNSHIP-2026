from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Application)
admin.site.register(Certificate)
admin.site.register(Applicant)
admin.site.register(EarlierAttendedCourse)
admin.site.register(Document)
admin.site.register(ContactMessage)
admin.site.register(CourseSchedule)