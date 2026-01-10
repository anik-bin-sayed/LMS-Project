from django.contrib import admin

from .models import (
    Category, Course
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    ordering=["id"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id', "category", "instructor", "title"]
    ordering=["id"]
