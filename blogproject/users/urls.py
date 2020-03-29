from django.urls import path
from . import views

urlpatterns = [
path('register/', views.register, name='register'),
path('deleted/', views.deleted, name='deleted'),
path('profile/', views.profile, name='profile'),
path('profile/delete/<int:pk>', views.delete.as_view(template_name='users/delete.html'), name='delete')
]