from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify
# Create your models here.

class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1200)
    excerpt = models.CharField(max_length=256)
    image = models.ImageField(upload_to='blog/post')
    author = models.CharField(max_length=255)
    tag = models.CharField(max_length=64)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    slug = models.SlugField(max_length=64, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    
# Convert title into slug.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
