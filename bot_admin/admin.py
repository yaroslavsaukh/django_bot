from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tg_id', 'name', 'gender')
    list_filter = ('gender',)
    list_display_links = ('pk', 'tg_id', 'name')
    search_fields = ('pk', 'tg_id')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at')
    list_filter = ('created_at',)
    list_display_links = ('pk', 'title')
    search_fields = ('pk', 'title')


admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)