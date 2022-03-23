from rest_framework import serializers
from .models import Home, About, Profile, Category, Skills, Project, Education

class HomeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    greetings_1 = serializers.CharField(max_length=5)
    greetings_2 = serializers.CharField(max_length=5)
    picture = serializers.ImageField(upload_to='picture/')
    updated = serializers.DateTimeField(auto_now_add=True)

    def create(self, validate_data):
        return Home.objects.create(**validate_data)

    def update(self, instance, validated_data):
        

    # class Meta:
    #     model = Home
    #     fields = '__all__'
