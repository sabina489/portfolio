from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    #path('', views.index, name='index'),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('education/',TemplateView.as_view(template_name="education.html")),
    path('skills/',TemplateView.as_view(template_name="skills.html")),
    path('projects/',TemplateView.as_view(template_name="projects.html")),
    path('contact/',TemplateView.as_view(template_name="contact.html")),

]