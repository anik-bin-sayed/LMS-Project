from django.urls import path
from .views import (
     CourseListCreateView,
     CourseDetailView,
     CategoryListView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('', CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
