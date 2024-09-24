from django.urls import path,include
from django.contrib import admin
from .views import *
admin.site.site_header = "Kollabo Admin"
admin.site.site_title  = "Kollabo TOOL"
admin.site.index_title = "Kollabo"

urlpatterns = [
    path('Ghunt/', ghunt_email_lookup, name='ghunt_email_lookup'),
]