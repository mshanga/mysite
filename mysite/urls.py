from django.contrib import admin
from django.urls import include, path
from . import views
from home import views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # path('', views.home, name='home'),
    path('', include('home.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('whatsapp/', include('whatsapp.urls')),     

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
]
