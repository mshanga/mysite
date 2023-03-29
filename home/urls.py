from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("features/", views.features, name="features"),
    path("faq/", views.faq, name="faq"),
]