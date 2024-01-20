from django.contrib import admin
from .models import CustomUser, Article


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_image', 'is_staff')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_update', 'published', 'user')


