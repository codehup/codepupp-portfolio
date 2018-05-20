from django.shortcuts import render
from .models import Job
from blog.models import Blog
# Create your views here.
def home(request):
    jobs = Job.objects
    blogs = Blog.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'blogs':blogs})
