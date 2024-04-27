from django.urls import path

from main import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("protected", view=views.protected, name="protected"),
]
