# from django.urls import reverse

# #Home view test
# def test_Home_list_view(self):
#     w = self.create_Home()
#     url = reverse("Home.views.Home")
#     resp = self.client.get(url)

#     self.assertEqual(resp.status_code, 200)
#     self.assertIn(w.name, resp.content)

# #About views test
# def test_About_list_view(self):
#     w = self.create_About()
#     url = reverse("About.views.About")
#     resp = self.client.get(url)

#     self.assertEqual(resp.status_code, 200)
#     self.assertIn(w.career, resp.content)

# #Projects views test
# def test_Project_list_view(self):
#     w = self.create_Project()
#     url = reverse("Project.views.Project")
#     resp = self.client.get(url)

#     self.assertEqual(resp.status_code, 200)
#     self.assertIn(w.image, resp.content)

# #Education views test
# def test_Education_list_view(self):
#     w = self.create_Education()
#     url = reverse("Education.views.Education")
#     resp = self.client.get(url)

#     self.assertEqual(resp.status_code, 200)
#     self.assertIn(w.year, resp.content)


# #Contact views test
# def test_Contact_list_view(self):
#     w = self.create_Contact()
#     url = reverse("Contact.views.Contact")
#     resp = self.client.get(url)

#     self.assertEqual(resp.status_code, 200)
#     self.assertIn(w.year, resp.content)

#Another way
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from sabina.models import Home,About,Education,Contact
import json

class TestViews(TestCase):
    def test_Home_GET(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['home1'])
        Home.objects.create(
            name='home1',

        )

    def test_HomeView(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sabina/home.html')
    
    def test_HomeDetail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sabina/home.html')

