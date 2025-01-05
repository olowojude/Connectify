from django.shortcuts import render, redirect
# Create your views here.


# Home page
def home(request):
    return render(request, "home.html")