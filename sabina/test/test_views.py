from django.test import TestCase
from django.urls import reverse
from django.test import TestCase
from sabina.models import Category, Education, Home,About,Project,Contact,Skills
from django.db import models
#Home view test
class HomeViewTest(TestCase):
    def create_home(self, name="test", greetings_1="hi",greetings_2="bye",picture="1",updated="now"):
        return Home.objects.create(name=name, greetings_1=greetings_1, greetings_2=greetings_2,picture=picture,updated=updated)
    def test_home_list_view(self):
        w = self.create_home()
        url = reverse("home-api")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(resp.data[0])

        self.assertIn(w.name, resp.data[0]["name"])

#Home detail view test
class HomeDetailViewTest(TestCase):
    def detail_home(self, name="test", greetings_1="hi",greetings_2="bye",picture="1",updated="now"):
        return Home.objects.create(name=name, greetings_1=greetings_1, greetings_2=greetings_2,picture=picture,updated=updated)
    def test_HomeDetail_GET(self):
        w = self.detail_home()
        url = reverse("detail-api", args=[w.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(resp.data)

        self.assertIn(w.name, resp.data["name"])
        #response = self.client.get(self.detail_url)
        #self.assertEquals(response.status_code, 200)
        #self.assertTemplateUsed(response, 'sabina/home.html')

#About views test
class AboutViewTest(TestCase):
    def create_about(self, heading="about", career="IT",description="about test",profile_img="upload",updated="now"):
        return About.objects.create(heading=heading, career=career,description=description,profile_img=profile_img,updated=updated)
    def test_about_list_view(self):
        w = self.create_about()
        #url = "https://localhost:8000/api/about/"
        url = reverse("about-api")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(resp.data[0])
        self.assertIn(w.career, resp.data[0]["career"])

#About detail view test
# class AboutDetailViewTest(TestCase):
#     def create_about(self, heading="about", career="IT",description="about test",profile_img="upload",updated="now"):
#         return About.objects.create(heading=heading, career=career,description=description,profile_img=profile_img,updated=updated)
        
#     def test_AboutDetail_GET(self):
#         w = self.detail_about()
#         url = reverse("detail-api", args=[w.id])
#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)
#         print(resp.data)

#         self.assertIn(w.career, resp.data["career"])
# Projects views test
class ProjectViewTest(TestCase):
    def create_Project(self, image="image", link="this is a link"):
        return Project.objects.create(image=image, link=link)
    def test_Project_list_view(self):
        w = self.create_Project()
        url = reverse("project-api")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(resp.data[0])
        self.assertIn(w.link, resp.data[0]["link"])

#Project detail test
# class ProjectDetailViewTest(TestCase):
#     def create_Project(self, image="image", link="this is a link"):
#         return Project.objects.create(image=image, link=link)
#     def test_ProjectDetail_GET(self):
#         w = self.detail_project()
#         url = reverse("detail-api", args=[w.id])
#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)
#         print(resp.data)

#         self.assertIn(w.image, resp.data["image"])

# #Education views test
class EducationViewTest(TestCase):
    def create_Education(self, year="year", level="education level"):
        return Education.objects.create(year=year,level=level)
    def test_Education_list_view(self):
        w = self.create_Education()
        url = reverse("education-api")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(resp.data[0])
        self.assertIn(w.year, resp.data[0]["year"])


# Contact views test
class ContactViewTest(TestCase):
    def create_Contact(self, phone="phone number", email="email address"):
        return Contact.objects.create(phone=phone,email=email)
    def test_Contact_list_view(self):
        w = self.create_Contact()
        url = reverse("contact-api")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(resp.data[0])
        self.assertIn(w.phone, resp.data[0]["phone"])

#Skills views test
# class CategoryViewTest(TestCase):
#     def create_Category(self, name="abc", updated="now"):
#         return Category.objects.create(name=name, updated=updated)
#     def test_Cotegory_list_view(self):
#         w = self.create_Category()
#         url = reverse("skills-api")
#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)
#         print(resp.data[0])
#         self.assertIn(w.name, resp.data[0]["name"])


# class SkillsViewTest(TestCase):
#     def create_Skills(self,category = "skills", skill_name= "html"):
#         return SKills.objects.create(category=category, skill_name=skill_name)



#Another way
# from urllib import response
# from django.test import TestCase, Client
# from django.urls import reverse
# from sabina.models import Home,About,Education,Contact
# import json

# class TestViews(TestCase):
#     def test_Home_GET(self):
#         self.client = Client()
#         self.list_url = reverse('list')
#         self.detail_url = reverse('detail', args=['home1'])
#         Home.objects.create(
#             name='home1',

#         )

#     def test_HomeView(self):
#         response = self.client.get(self.list_url)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'sabina/home.html')
    
#     def test_HomeDetail_GET(self):
#         response = self.client.get(self.detail_url)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'sabina/home.html')

