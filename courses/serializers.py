from rest_framework import serializers
from .models import Course, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.username')
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'category','category_detail', 'title', 'description', 'instructor', 'created_at', 'updated_at']
