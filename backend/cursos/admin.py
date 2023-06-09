from django.contrib import admin

from .models import Course, Rating


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at', 'active')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'evaluator_name', 'email',
                    'note', 'created_at', 'updated_at', 'active')
