from django import forms
from .models import User, Recruiter, Jobseeker, JobPost
from django.contrib.auth.forms import UserCreationForm



class RecruiterSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User 


    def save(self):
        user = super().save(commit=False)
        user.is_recruiter = True
        user.save()
        recruiter = Recruiter.objects.create(user=user)
        return user


class JobseekeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 

    def save(self, commit=True):
        user = super().user(commit=False)
        user.is_jobseeker = True
        user.save()
        jobseeker = Jobseeker.objects.create(user=user)
        return user

    