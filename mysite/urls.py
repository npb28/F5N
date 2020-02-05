from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls), # Looks for admin view
    path('', include('contacts.urls')), # Directs traffic to contacts url
]                                       # and looks for further instructions
