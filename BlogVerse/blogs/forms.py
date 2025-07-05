from django import forms
from .models import BlogModel


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ("title", "content","excerpt","image","author","tag")

        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Title"}),
            'content': forms.Textarea(attrs={"class":"form-control", "placeholder":"Start Writing.."}),
            'excerpt': forms.Textarea(attrs={"class":"form-control","placeholder":"short description"}),
            'image': forms.FileInput(attrs={"class":"form-control"}),
            'author': forms.TextInput(attrs={"class":"form-control"}),
            'tag': forms.TextInput(attrs={"class":"form-control"}),
        }