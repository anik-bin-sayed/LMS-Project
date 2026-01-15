from django.urls import path
from .views import LessonListCreateView, LessonDetailView,StudentLessonDetailView

urlpatterns = [
    path('', LessonListCreateView.as_view(), name='lesson-list'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('student/<int:pk>/', StudentLessonDetailView.as_view(), name='student-lesson-detail'),
]
