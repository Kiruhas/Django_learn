from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import admin
from .forms import UserForm
from .models import Post

admin.site.register(Post)

def index(request):
  return render(request, "index.html", context={"n":5})

def about(request):
  title = "Django Learning"
  user = {"name" : "Kirill", "age" : 23}
  langs = ["Russian", "English"]
  data = {"title": title, "user" : user, "langs":langs}
  return TemplateResponse(request, "metanitapp/about.html", context=data)

def contact(request):
  return TemplateResponse(request, "contact.html", context = {"title":"Контакты"})

def products(request, product_id = 0):
  try:
    category = request.GET.get("cat", "")
  except AttributeError:
    pass
  
  output = "Error: no product id get!" if product_id == False else "<h3>Product № {0}, category: {1}</h3>".format(product_id, category)
  return HttpResponse(output)

def userform(request):
  if request.method == "POST":
    user_form = UserForm(request.POST)
    if user_form.is_valid():
      name = user_form.cleaned_data["name"]
      return HttpResponse("<h3>Hello, {0}</h3>".format(name))
    else:
      return HttpResponse("<h3>Invalid data!</h3>")
  else:
    user_form = UserForm()
    return render(request, "userform.html", {"form":user_form})

def posts(request):
  context = {
    'title': "Все посты",
    'posts': Post.objects.all(),
  }
  return render(request, "posts.html", context)

