# from django.shortcuts import render
# from .models import Home, About, Profile, Category, Skills, Project, Education
# from django.views.generic import TemplateView

# #rest framework
# #from django.shortcuts import render



# def index(request):

#      # Home
#     home = Home.objects.latest('updated')

#     # About
#     about = About.objects.latest('updated')
#     profiles = Profile.objects.filter(about=about)

#      # Skills
#     categories = Category.objects.all()

#     # Projects
#     project = Project.objects.all()

#     #Education
#     education = Education.objects.all()

#     context = {
#         'home': home,
#         'about': about,
#         'profiles': profiles,
#         'categories': categories,
#         'project': project,
#         'education': education
#     }

    
#     return render(request, 'index.html', context)

from pipes import Template
from typing import List
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.views.generic.list import ListView
from .models import About, Category, Education, Home, Project, Skills, Contact
from .serializers import AboutSerializer, HomeSerializer, ContactSerializer, ProjectSerializer, EducationSerializer, SkillsSerializer
from rest_framework import generics

from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)

#Home Section
class HomeListView(ListView):
    template_name = 'home.html'
    context_object_name = 'home'

    def get_queryset(self):
        """Return the last five published questions."""
        return Home.objects.latest('updated')

#create home section
class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

        
# class HomeListView(ListView):
#     model = Home

#About Section
class AboutListView(ListView):
    template_name = 'about.html'
    context_object_name = 'about'

    def get_queryset(self):
        """Return the last five published questions."""
        return About.objects.latest('updated')
#Create About
class AboutList(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

#Retrieve about section
class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



# #Create
# class AboutCreateView(ListView):
#     template_name = 'about.html'
#     context_object_name = 'about'

#     def get_queryset(self):
#         return About.objects.latest('created')


#Skills Section
class SkillsListView(ListView):
    template_name = 'skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Skills.objects.all()

#Create skills
class SkillsList(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = SkillsSerializer

#Retrieve skills section
class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = SkillsSerializer

#Contact Section
class ContactListView(ListView):
    template_name = 'contact.html'
    context_object_name = 'contact'

    def get_queryset(self):
        return Contact.objects.all()

#Create Contact section
class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

#Retrieve contact section
class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
        

#Education section
class EducationListView(ListView):
    template_name = 'education.html'
    context_object_name = 'education'

    def get_queryset(self):
        
        return Education.objects.all()

#Create Education section
class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

#Retrieve education section
class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = EducationSerializer



#Projects section
class ProjectListView(ListView):
    template_name = 'projects.html'
    context_object_name = 'project'

    def get_queryset(self):
        project = Project.objects.all()

#Create Project section
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

#Retrieve project section
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
        
#Api of AboutSerializer
class AboutListAPIView(ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

#Api of ProjectSerializeer
class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

#Api of SkillsSerializer
class SkillsListAPIView(ListAPIView):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()

#Api of HomeSerializer
class HomeListAPIView(ListAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()

#Api of EducationSerializer
class EducationListAPIView(ListAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

#Api of ContactSerializer
class ContactListAPIView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

# class AboutListView(ListView):
#     model = About

# class SkillsListView(ListView):
#     model = Skills

# class ProjectListView(ListView):
#     model = Project

# class EducationListView(List):
#     model = Education

    