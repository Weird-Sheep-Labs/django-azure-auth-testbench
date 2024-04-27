from azure_auth.decorators import azure_auth_required
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


@azure_auth_required
def protected(request):
    return HttpResponse("Protected")
