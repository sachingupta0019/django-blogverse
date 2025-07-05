from django.urls import path
from blogs import views


urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:slug>', views.post, name="post"),
    path('create', views.create_post, name="add-post"),
    path('edit/<str:slug>', views.edit_post, name="edit-post"),
    path('delete/<str:slug>', views.delete_post, name='delete-post'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('about', views.About_Us, name="about-us"),
    path('contact', views.Contact_Us, name="contact-us"),
    
]
