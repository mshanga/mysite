from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def features(request):
    return render(request, "features.html")

def faq(request):
    return render(request, "faq.html")