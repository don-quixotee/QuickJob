from ..models import JobPost
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = JobPost
    template_name = 'jobapp/jobseeker/home.html'
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = JobPost
    tempalte_name = 'jobapp/jobseeker/detail.html'
    