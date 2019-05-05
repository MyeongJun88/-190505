from django.urls import path, include
from . import views


urlpatterns = [

    path('login/', views.login, name="login"),
    path('edituser/', views.edituser, name="edituser"),
    path('writing/', views.writing, name="writing"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('edituser/<int:id>/', views.edituser, name="edituser"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
]