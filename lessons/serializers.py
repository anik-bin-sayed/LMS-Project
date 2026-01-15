from rest_framework import serializers
from .models import Lesson
from courses.serializers import CourseSerializer

class LessonSerializer(serializers.ModelSerializer):
    category_detail = CourseSerializer(source='course', read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
