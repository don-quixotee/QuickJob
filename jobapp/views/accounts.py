from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from ..models import Recruiter, Jobseeker, User, JobPost
from ..forms import RecruiterSignUpForm, JobseekeSignUpForm


# Create your views here.


class SignUpView(TemplateView):
    template_name = 'registration/signUp.html'


class RecruiterSignUpView(CreateView):
    model = User 
    form_class = RecruiterSignUpForm
    template_name = 'registration/recruiter_SignUp.html'


class JobseekerSignUpView(CreateView):
    model = User
    form_class = JobseekeSignUpForm
    template_name = 'registration/jobseeker_SignUp.html'