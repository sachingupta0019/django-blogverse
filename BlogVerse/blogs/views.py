from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import BlogModel
from .forms import CreatePostForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404



# Home Page
def home(request):
    blogs = BlogModel.objects.all().order_by("-created_at")
    return render(request, "blogs/home.html", {'blogs':blogs})

def post(request, slug):
    post = BlogModel.objects.get(slug=slug)
    return render(request, "blogs/post.html",{'post':post})

def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            new_post = CreatePostForm(request.POST, request.FILES)
            if new_post.is_valid():
                new_post.save()
                messages.success(request, "Post has been created.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalide data..")
        else:
            new_post = CreatePostForm()
        return render(request, "blogs/new-post.html",{'new_post':new_post})
    else:
        return HttpResponseRedirect("/user/login")
    
def edit_post(request, slug):
    blog = BlogModel.objects.get(slug=slug)
    if request.method == "POST":
        edit_post = CreatePostForm(request.POST,request.FILES, instance=blog)
        if edit_post.is_valid():
            messages.success(request, "Post updated.!!!")
            edit_post.save()
            return redirect('post', slug=blog.slug)
    else:
        edit_post = CreatePostForm(instance=blog)
    return render(request, "blogs/new-post.html",{"new_post":edit_post})

def delete_post(request, slug):
    post = get_object_or_404(BlogModel, slug=slug)
    print(post)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post Deleted")
    return HttpResponseRedirect("/dashboard")


# User Dashboard
def dashboard(request):
    blogs = BlogModel.objects.all()
    return render(request, "blogs/dashboard.html",{"blogs":blogs})

# About-US
def About_Us(request): 
    return render(request, "blogs/about.html")

#Contact-Us
def Contact_Us(request):
    return render(request, "blogs/contact.html")