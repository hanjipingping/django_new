from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user),
    path('user1/', views.MO.as_view())
]
