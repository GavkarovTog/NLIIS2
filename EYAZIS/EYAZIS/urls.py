from django.urls import path
from Project_2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dependency/', views.dependency, name='dependency'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('upload_text', views.upload_text, name='upload_text'),
]