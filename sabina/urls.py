from unicodedata import name
from django.urls import path
from sabina import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from .views import (
    AboutListView,
    HomeListView,
    AboutListAPIView,
    ContactListAPIView,
    ProjectListView,
    EducationListView,
    SkillsListView,
    ContactListView,
    ProjectListAPIView,
    SkillsListAPIView,
    HomeListAPIView,
)



urlpatterns = [
    
    #path('', views.index, name='index'),
    #home section
    path('home/', HomeListView.as_view()),
    path('api/home', HomeListAPIView.as_view(),name="home-api"),
    path('api/home/create', views.HomeList.as_view()),
    path('api/home/<int:pk>/', views.HomeDetail.as_view(),name="detail-api"),

    #About section
    path('about/', AboutListView.as_view()),
    path('api/about', AboutListAPIView.as_view(),name="about-api"),
    path('api/about/create', views.AboutList.as_view()),
    path('api/about/<int:pk>/', views.AboutDetail.as_view()),
    
    
    #Projects sections
    path('project/', ProjectListView.as_view()),
    path('api/project', ProjectListAPIView.as_view(), name="project-api"),
    path('api/project/create', views.ProjectList.as_view()),
    path('api/project/<int:pk>/', views.ProjectDetail.as_view()),
   

    #Education section
    path('education/', EducationListView.as_view()),
    path('api/education/create', views.EducationList.as_view(), name="education-api"),
    path('api/education/<int:pk>/', views.EducationDetail.as_view()),

    #Skills section
    path('skills/', SkillsListView.as_view()),
    path('api/skills', SkillsListAPIView.as_view()),
    path('api/skills/create', views.SkillsList.as_view(), name="skills-api"),
    path('api/skills/<int:pk>/', views.SkillsDetail.as_view()),
    #path('contact/', ContactListView.as_view()),
    path('portfolio/', ProjectListView.as_view()),

    #contact section
    path('contact/', ContactListView.as_view()),
    path('api/contact', ContactListAPIView.as_view()),
    path('api/contact/create', views.ContactList.as_view(), name="contact-api"),
    path('api/contact/<int:pk>/', views.ContactDetail.as_view()),

    # path('education/',TemplateView.as_view(template_name="education.html")),
    # path('skills/',TemplateView.as_view(template_name="skills.html")),
    #path('project/',TemplateView.as_view(template_name="projects.html")),
    # path('contact/',TemplateView.as_view(template_name="contact.html")),

    #Index section
    path('index/',TemplateView.as_view(template_name="index.html")),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)