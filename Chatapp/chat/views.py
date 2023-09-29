from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
# tebe bala check mikone va agar karbar auth nashode bashe ono redirect mikone be safhe login
    context = {}
    return render(request, "chat/chatPage.html", context)
# context ye dict khaliye ke vorodi ha tosh rikhte mishan.render ham ke file html ro mikhone.context ye parametre.
    
    
