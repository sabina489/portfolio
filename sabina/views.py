from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Project, Education

#rest framework
#from sabina.models import Sabina



def index(request):

     # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

     # Skills
    categories = Category.objects.all()

    # Projects
    project = Project.objects.all()

    #Education
    education = Education.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'project': project,
        'education': education
    }

    
    return render(request, 'index.html', context)