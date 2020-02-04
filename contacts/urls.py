from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('create/new/', views.create_new, name='create_new'),
]
