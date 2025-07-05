from django.contrib import admin
from .models import BlogModel

# Register your models here.
@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt", "content","author","tag","image","rating","comment","slug","created_at","updated_at")
    

    def __str__(self):
        return self.title