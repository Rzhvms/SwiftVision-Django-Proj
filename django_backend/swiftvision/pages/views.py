from django.shortcuts import render
from django.http import HttpResponse
  

def index(request):
    return render(request, "main_page.html")

def statisctic(request):
    return render(request, "statistic.html")

def demand(request):
    return render(request, "demand.html")

def geography(request):
    return render(request, "geography.html")

def skills(request):
    return render(request, "skills.html")

def vacancies(request):
    return render(request, "vacancies.html")