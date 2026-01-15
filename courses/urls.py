from django.urls import path
from .views import (
     CourseListCreateView,
     CourseDetailView,
     CategoryListView,
     UpdateCategoryView,
     UpdateRetrieveCourseView
)

urlpatterns = [
    # category
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path("update-category/<int:pk>/", UpdateCategoryView.as_view(), name="update-category"),

    # course
    path('', CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path("update-course/<int:pk>/", UpdateRetrieveCourseView.as_view(), name="update-retrieve-course")
]
