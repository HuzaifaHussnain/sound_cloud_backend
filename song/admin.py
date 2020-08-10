from django.contrib import admin
from .models import Song, Comment

class CommentInline(admin.StackedInline):
	model = Comment

class SongAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

admin.site.register(Song, SongAdmin)
