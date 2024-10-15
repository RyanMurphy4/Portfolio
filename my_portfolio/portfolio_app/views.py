import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings

projects = [
{
    'title': "Queue Manager",
    "description": [
    'Developed a Python-based application to monitor a specific region of another applications interface.',
    'Integrated Optical Character Recognition (OCR) to extract and analyze text from the monitored region.',
    'Implemented logic to compare the OCR results with a predefined string.',
    'Upon detecting a match, the application sends a simulated keypress to interact with the monitored application.',
    ],
    "image_url" : 'portfolio_app/images/manager.png',  
    "github_url": 'https://github.com/RyanMurphy4/queue_manager',
    "project_url": ""
},

{
    'title': "Dnd Vendor",
    "description": [
    "Created a script that automates checking the stats of vendor-sold items (craftables) to determine whether they are worth purchasing.",
    "Utilized a list of vendors and items of interest for automated analysis.",
    "Employed template matching to identify items in the vendor's inventory.",
    "Integrated mouse automation to move to the location of identified items.",
    "Used image pre-processing and contour matching techniques to detect the region where item stats are displayed.",
    "Applied OCR to extract item stats and generate an object to assess if the item meets the desired criteria for purchase.",
    "Note: The script is no longer functional as item stats are hidden before purchase.",
    ],
    "image_url" : 'portfolio_app/images/vendor_code.png',  
    "github_url": 'https://github.com/RyanMurphy4/dnd_vendor',
    "project_url": ""
},
{
    'title': "Foxhole Auto Digger",
    "description": [
    'Collected and annotated a dataset of images for object detection in a game.',
    'Trained a custom YOLO model to detect in-game objects.',
    'Developed an algorithm to determine the closest detected object relative to the in-game character and move to it.',
    'Utilized Object-Oriented Programming (OOP) to manage states, such as tracking whether the character is performing an action on the object.',
    'Automated the process of detecting, moving to, and interacting with in-game items through a custom Python script.',
    ],
    "image_url" : 'portfolio_app/images/digging.gif',  
    "github_url": 'https://github.com/RyanMurphy4/Foxhole-Auto-Dig',
    "project_url": ""
}

]

languages = [
    {"name": "Python",
     "image": "portfolio_app/images/python_logo.png"},

     {"name": "Javascript",
     "image": "portfolio_app/images/javascript_logo.png"},

     {"name": "Rust",
     "image": "portfolio_app/images/rust_logo.png"},

     {"name": "Java",
     "image": "portfolio_app/images/java_logo.png"},

    #  {"name": "Python",
    #  "image": "portfolio_app/images/python_logo.png"},

    #  {"name": "Python",
    #  "image": "portfolio_app/images/python_logo.png"},

    #  {"name": "Python",
    #  "image": "portfolio_app/images/python_logo.png"},
]

frameworks = [
    {"name": "Django",
     "image": "portfolio_app/images/django_logo.png"},

     {"name": "Flask",
     "image": "portfolio_app/images/flask_logo.png"},

     {"name": "Selenium",
     "image": "portfolio_app/images/selenium_logo.png"},
     


]
# Create your views here.
def index(request):
    
    return render(request, 'portfolio_app/index.html', {
        "languages": languages,
        "frameworks": frameworks,
    })

def project_list(request):


    return render(request, 'portfolio_app/projects.html', {
        "projects": projects
    })

def resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'portfolio_app', 'static', 'portfolio_app', 'resume.pdf')
    

    return FileResponse(open(file_path, 'rb'), content_type="application/pdf")

