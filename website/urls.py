from . import views
from .views import index, UserRegisterView
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('register/', UserRegisterView.as_view(), name='register'),
]
