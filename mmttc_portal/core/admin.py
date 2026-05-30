from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Document)
admin.site.register(Certificate)