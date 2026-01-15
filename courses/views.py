from rest_framework import generics, permissions

from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer
from .permissions import IsTeacherOrReadOnly, IsStudentOrReadOnly

# teacher and admin
class CategoryListView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsTeacherOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsTeacherOrReadOnly]

class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsTeacherOrReadOnly]




# Teacher and admin 
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

# teacher and admin
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrReadOnly]

class UpdateRetrieveCourseView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrReadOnly]