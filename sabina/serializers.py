from rest_framework import serializers
from .models import Home, About, Profile, Category, Skills, Project, Education


#home
class HomeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    greetings_1 = serializers.CharField(max_length=5)
    greetings_2 = serializers.CharField(max_length=5)
    picture = serializers.ImageField(upload_to='picture/')
    updated = serializers.DateTimeField(auto_now_add=True)

    def create(self, validate_data):
        return Home.objects.create(**validate_data)

    #def update(self, instance, validated_data):

         # class Meta:
    #     model = Home
    #     fields = '__all__'

#About
class AboutSerializer(serializers.ModelSerializer):
    heading = serializers.CharField(max_length=50)
    career = serializers.CharField(max_length=30)
    description = serializers.TextField(blank=False)
    profile_img = serializers.ImageField(upload_to='profile/')
    
    updated = serializers.DateTimeField(auto_now=True)

    def create(self, validate_data):
        return About.objects.create(**validate_data)



#Profile
class ProfileSerializer(serializers.Model):
    about = serializers.ForeignKey(About,
                                on_delete=serializers.CASCADE)
    social_name = serializers.CharField(max_length=10)
    link = serializers.URLField(max_length=200)

    def create(self, validate_data):
        return Profile.objects.create(**validate_data)
    


#Skills
class SkillsSerializer(serializers.Model):
    category = serializers.ForeignKey(Category,
                                on_delete=serializers.CASCADE)
    skill_name = serializers.CharField(max_length=20)
    
    def create(self, validate_data):
        return Skills.objects.create(**validate_data)


#Education
class EducationSerailizer(serializers.Model):
    year = serializers.CharField(max_length=50)
    level = serializers.CharField(max_length=80)

    def create(self, validate_data):
        return Education.objects.create(**validate_data)