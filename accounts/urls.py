from django.urls import path
from . import views

urlpatterns = [
    path('edituser/', views.edituser, name='edituser'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]