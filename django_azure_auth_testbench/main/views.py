import datetime

from azure_auth.decorators import azure_auth_required
from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


@azure_auth_required
def protected(request):
    token_expiry = datetime.datetime.fromtimestamp(
        request.session["id_token_claims"]["exp"]
    )
    return render(
        request, "main/protected.html", context={"token_expiry": token_expiry}
    )
