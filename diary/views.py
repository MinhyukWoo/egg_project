from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, "diary/index.html", {"url": request.get_host()})


def chatting(request):
    return render(request, "diary/chatting.html")


def feedback(request):
    return render(request, "diary/feedback.html")
