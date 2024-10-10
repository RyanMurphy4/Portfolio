from django.shortcuts import render
from django.http import HttpResponse

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
    "Created a script that automates checking the stats of vendor-sold items (craftables) to determine whether they are worth purchasing.",
    "Utilized a list of vendors and items of interest for automated analysis.",
    "Employed template matching to identify items in the vendor's inventory.",
    "Integrated mouse automation to move to the location of identified items.",
    "Used image pre-processing and contour matching techniques to detect the region where item stats are displayed.",
    "Applied OCR to extract item stats and generate an object to assess if the item meets the desired criteria for purchase.",
    "Note: The script is no longer functional as item stats are hidden before purchase.",
    ],
    "image_url" : 'portfolio_app/images/digging.gif',  
    "github_url": 'https://github.com/RyanMurphy4/dnd_vendor',
    "project_url": ""
}

]

# Create your views here.
def index(request):
    numbers = [i for i in range(10)]
    return render(request, 'portfolio_app/index.html', {
        "nums": numbers
    })

def project_list(request):


    return render(request, 'portfolio_app/projects.html', {
        "projects": projects
    })