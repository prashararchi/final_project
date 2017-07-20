# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from demoapp.forms import SignUpForm
from demoapp.models import UserModel
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup_view(request):

    if request.method == "GET" :
        signup_form = SignUpForm()
        return render(request,"signup_1.html" , {'signup_form': signup_form})
    elif request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            name = signup_form.cleaned_data['name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            #save user to DATABASE...
            user = UserModel(name = name,username=username,email=email,password=make_password(password))
            user.save()
        return render(request, "registered.html", {'signup_form': signup_form})

