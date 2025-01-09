from django.shortcuts import render, redirect

from .models import Link, User
from .forms import RegisterForm, UserForm, AddLinkForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Home page
def home(request):
    return render(request, "home-page.html")

# User registration page
def register(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        registerform = RegisterForm()

        if request.method == "POST":
            registerform = RegisterForm(request.POST)
            if registerform.is_valid():
                registerform.save()
                messages.success(request, "Account was created successfully")
                return redirect("loginpage")

        context = {"registerform": registerform}
        return render(request, "register-form.html", context)
    

# Login page
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin')
            else:
                messages.info(request, "Username or Password is incorrect")

        context = {}
        return render(request, "login-page.html", context)
    

# Logout page
def logoutpage(request):
    logout(request)
    return redirect('loginpage')

# Admin page view
@login_required(login_url="loginpage")
def admin(request):
    links = Link.objects.filter(user=request.user)

    context = {
        "links": links
    }
    return render(request, "admin-page.html", context)


# Add link view
@login_required(login_url="loginpage")
def addlink(request):

    if request.method == "POST":
        addlinkform = AddLinkForm(request.POST)
        if addlinkform.is_valid():
            form = addlinkform.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('admin')
    else:
        addlinkform = AddLinkForm()

    context = {"addlinkform": addlinkform}
    return render(request, "add-link-page.html", context)


# Update link view
@ login_required(login_url="loginpage")
def updatelink(request, pk):
    updatelink = Link.objects.get(id=pk)
    updatelinkform = AddLinkForm(instance=updatelink)

    if request.method == "POST":
        updatelinkform = AddLinkForm(request.POST, instance=updatelink)
        if updatelinkform.is_valid():
            updatelinkform.save()
            return redirect('admin')

    context = {"updatelinkform": updatelinkform}
    return render(request, "update-link-page.html", context)


# Delete link view
@ login_required(login_url="loginpage")
def deletelink(request, pk):
    deletelink = Link.objects.get(id=pk)
    if request.method == 'POST':
        deletelink.delete()
        return redirect("admin")

    context = {"deletelink": deletelink}
    return render(request, "delete-link-page.html", context)


# Preview page view
def preview(request, username):
    username = User.objects.get(username=username)
    links = Link.objects.filter(user=request.user)

    context = {
        "links": links
    }
    return render(request, "preview-page.html", context)
