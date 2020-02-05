from django.urls import path
from . import views

# urls that point to views
urlpatterns = [
    path('', views.post_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    # Expects int value that it will then transfer to views as a variable called pk
    path('create/new/', views.create_new, name='create_new'),
]
