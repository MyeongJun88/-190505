from django.urls import path
from. import views

urlpatterns = [
    path('login/', views.login, name="login"),
    # path('edituser/', views.edituser, name="edituser"),
    path('writing/', views.writing, name="writing"),
    # path('detail/<int:post_id>', views.detail, name="detail"),
]