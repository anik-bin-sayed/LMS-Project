from rest_framework import serializers
from .models import Course, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.username')

    class Meta:
        model = Course
        fields = ['id', 'category', 'title', 'description', 'instructor', 'created_at', 'updated_at']
