from django.shortcuts import render
from django.http import HttpResponse
from .models import Business


proj = [
     {
        "ProjectID": 1,
        "BusinessID": 101,
        "Title": "Website Development",
        "Description": "Develop a responsive website for an e-commerce platform.",
        "RequiredSkills": "HTML, CSS, JavaScript, Django",
        "Budget": 5000.00,
        "Deadline": "2024-12-01",
        "Status": "Open",
        "PostDate": "2024-10-10"
    },
    {
        "ProjectID": 2,
        "BusinessID": 102,
        "Title": "Mobile App Development",
        "Description": "Create a cross-platform mobile app for online shopping.",
        "RequiredSkills": "React Native, Firebase, UI/UX Design",
        "Budget": 8000.00,
        "Deadline": "2024-11-15",
        "Status": "In Progress",
        "PostDate": "2024-09-28"
    },
    {
        "ProjectID": 3,
        "BusinessID": 103,
        "Title": "SEO Optimization",
        "Description": "Optimize website content for better search engine rankings.",
        "RequiredSkills": "SEO, Content Writing, Digital Marketing",
        "Budget": 1500.00,
        "Deadline": "2024-10-30",
        "Status": "Closed",
        "PostDate": "2024-09-05"
    }
]


def home(request):
    return  render(request,'home/index.html')
def login(request):
    return  render(request,'home/login.html')

def business(request):
    businesses = Business.objects.all()
    context ={
        'businesses' : businesses
    }
    return render(request,'home/business.html',context)

def projects(request):
    context = {
        'projects' : proj
    }
   

    return render(request,'home/project.html',context)


