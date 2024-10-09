from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    numbers = [i for i in range(10)]
    return render(request, 'portfolio_app/index.html', {
        "nums": numbers
    })

def project_list(request):

    projects = [
    {
        'title': "Project name",

        "description": 
        
        '''
        Long project description
        is going to be here
        on multiple lines
        ..weird
        smile
        ''',

        "image_url" : 'portfolio_app/static/portfolio_app/images/project1.png',  #OPTIONAL
        "github_url": 'GITHUB_URL',
        "project_url": "ACTUAL WEBSITE URL"
    },

    ]

    return render(request, 'portfolio_app/projects.html', {
        "projects": projects
    })