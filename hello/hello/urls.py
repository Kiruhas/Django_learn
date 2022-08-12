from django.contrib import admin
from django.urls import path
from django.urls import re_path
from metanitapp import views
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^products$', views.products),
    re_path(r'^products/(?P<product_id>\d+)', views.products),
    re_path(r'^about/contact', TemplateView.as_view(template_name="contact.html", extra_context = {"title":"Contacts"})),
    re_path(r'^about/', views.about, name="About"),
    re_path(r'^posts/', views.posts, name="posts"),
    path('userform/', views.userform, name="userform"),
    path('admin/', admin.site.urls),
    path('', views.index, name="Home"),
]
