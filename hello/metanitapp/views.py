from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

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
