from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    numbers = [i for i in range(100)]
    return render(request, 'portfolio_app/index.html', {
        "nums": numbers
    })

def projects(request):
    return render(request, 'portfolio_app/projects.html', {
        "nothing": "NOTHING"
    })