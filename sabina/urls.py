from django.urls import path
from sabina import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from .views import (
    AboutListView,
    HomeListView,
    AboutListAPIView,
    ProjectListView,
    EducationListView,
    SkillsListView,
    ContactListView,
    
    

)



urlpatterns = [
    #path('', views.index, name='index'),
    #About section
    path('home/', HomeListView.as_view()),
    path('api/about', AboutListAPIView.as_view()),
    path('api/about/create', views.AboutList.as_view()),
    path('api/about/<int:pk>/', views.AboutDetail.as_view()),
    
    #Projects sections
    # path('api/project/create', views.ProjectList.as_view()),
    # path('api/project/<int:pk>/', views.ProjectDetail.as_view()),
    # path('about/',TemplateView.as_view(template_name="about.html")),
    path('about/', AboutListView.as_view()),
    path('education/', EducationListView.as_view()),
    path('skills/', SkillsListView.as_view()),
    #path('contact/', ContactListView.as_view()),
    path('portfolio/', ProjectListView.as_view()),
    path('contact/', ContactListView.as_view()),

    # path('education/',TemplateView.as_view(template_name="education.html")),
    # path('skills/',TemplateView.as_view(template_name="skills.html")),
    # path('projects/',TemplateView.as_view(template_name="projects.html")),
    # path('contact/',TemplateView.as_view(template_name="contact.html")),
    # path('index/',TemplateView.as_view(template_name="index.html")),

]

urlpatterns = format_suffix_patterns(urlpatterns)