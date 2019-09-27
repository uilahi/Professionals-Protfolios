from django.shortcuts import render
from Python_Django.protfolio_second_project.jobs.models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
