from django.contrib import admin
from categories.models import Category


# Register your models here.
@admin.register(Category)
class CateforyAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
