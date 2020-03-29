from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('like/', views.likes, name='like'),
    path('article/<int:id>/<slug:slug>/', views.slug, name='slug')
]