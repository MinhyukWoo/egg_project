from django.urls import path
from . import views

app_name = "diary"

urlpatterns = [
    path("", views.index, name="index"),
    path("chatting", views.chatting, name="chatting"),
    path("feedback", views.feedback, name="feedback"),
]
