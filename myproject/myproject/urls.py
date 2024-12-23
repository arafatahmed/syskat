
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
   re_path(r'^login/', admin.site.urls),
   re_path('', include('main.urls')),
]
