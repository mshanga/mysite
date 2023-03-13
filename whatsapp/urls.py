from django.urls import include, path
from . import views

app_name = 'whatsapp'
urlpatterns = [
    path('whatsapp/', views.whatsapp, name='whatsapp'),
]