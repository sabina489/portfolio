# from django.test import TestCase
# from sabina.models import Category, Education, Home,About,Project,Contact

# #from django.utils import timezone
# from django.db import models

# #Home Models test
# class HomeTest(TestCase):

#     def create_Home(self, name="test", greetings_1="hi",greetings_2="bye",picture="1",updated="now"):
#         return Home.objects.create(name=name, greetings_1=greetings_1, greetings_2=greetings_2,picture=picture,updated=updated)
    

#     # def __str__(self):
#     #     return self.name

#     def test_Home_creation(self):
#         w = self.create_Home()
#         self.assertEqual(w.__str__(), w.name)

# #About model test
# class AboutTest(TestCase):
#     def create_About(self, heading="about", career="about",description="about test",profile_img="upload",updated="now"):
#         return About.objects.create(heading=heading, career=career,description=description,profile_img=profile_img,updated=updated)
    
    
#     def test_About_creation(self):
#         w = self.create_About()
#         self.assertEqual(w.__str__(), w.career)
 

#  #Profile model test
# #  class ProfileTest(TestCase):

# #      def create_Profile(self, about="profile", social_name="name",link="link"):
# #          return Profile.objects.create(about=about,social_name=social_name,link=link)


# #Skills model test
# class CategoryTest(TestCase):
#     def create_Category(self, name="name", updated="now"):
#         return Category.objects.create(name=name, updated=updated)

#     def test_Category_creation(self):
#         w = self.create_Category()
#         self.assertEqual(w.__str__(), w.name)

# #Portfolio model test
# class ProjectTest(TestCase):
#     def create_Project(self, image="image", link="this is a link"):
#         return Project.objects.create(image=image, link=link)

#     def test_Project_creation(self):
#         w = self.create_Project()
#         self.assertEqual(w.__str__(), f'Project {w.id}')

# #Education model test
# class EducationTest(TestCase):
#     def create_Education(self, year="year", level="education level"):
#         return Education.objects.create(year=year,level=level)

#     def test_Education_creation(self):
#         w = self.create_Education()
#         self.assertEqual(w.__str__(),f'Education {w.id}')

# #Contact model test
# class ContactTest(TestCase):
#     def create_Contact(self, phone="phone number", email="email address"):
#         return Contact.objects.create(phone=phone,email=email)
    
#     def test_Contact_creation(self):
#         w = self.create_Contact()
#         self.assertEqual(w.__str__(),w.phone)

#Testing the API
# from tastypie.test import ResourceTestCase

# class EntryResourceTest(ResourceTestCase):

#     def test_get_api_json(self):
#         resp = self.api_client.get('/api/home/', format='json')
#         self.assertValidJSONResponse(resp)

#     def test_get_api_xml(self):
#         resp = self.api_client.get('/api/home/', format='xml')
#         self.assertValidXMLResponse(resp)
    
#Testing the API
# from tastypie.test import ResourceTestCase

# class AboutResourceTest(ResourceTestCase):

#     def test_get_api_json(self):
#         resp = self.api_client.get('api/about', format = 'json')
#         self.assertValidJSONResponse(resp)

#     def test_get_api_xml(self):
#         resp = self.api_client.get('/api/about', format='xml')
#         self.assertValidXMLResponse(resp)

