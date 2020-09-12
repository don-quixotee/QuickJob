from django.urls import path
from .views.accounts import SignUpView, RecruiterSignUpView , JobseekerSignUpView
from .views.jobseeker import HomeView



urlpatterns = [
    path('SignUp/', SignUpView.as_view(), name='signUp'),
    path('SignUp/recruiter/', RecruiterSignUpView.as_view(), name='recruiter-SignUp'),
    path('SignUp/jobseeker/', JobseekerSignUpView.as_view(), name='jobseeker-SignUp'),
    path('', HomeView.as_view(), name='home')

]
