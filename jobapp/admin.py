from django.contrib import admin
from .models import JobPost, User, Recruiter, Jobseeker

# Register your models here.
admin.site.register(User)
admin.site.register(Recruiter)
admin.site.register(Jobseeker)
admin.site.register(JobPost)



