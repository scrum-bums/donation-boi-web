from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django import forms
import json,datetime
from django.contrib.auth.models import User, Group # need to import Group from https://stackoverflow.com/a/6288863/5434744
import random, string
from django.contrib.auth import logout
from .models import Store, Item
from django import urls
from .forms import RegistrationForm, SearchStoresForm
from django.contrib.auth import authenticate, login

class StoreList(ListView):
    model = Store
    context_object_name = "stores"

class StoreDetailView(DetailView):
    model = Store
    context_object_name = "store"
    template_name = "donation_boi/store_detail.html"

class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"
    template_name = "donation_boi/item_detail.html"

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # create account
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        username=form.cleaned_data['username'])
            # sign in user
            new_user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, new_user)
                return HttpResponseRedirect("/")
            return HttpResponseServerError()
    else:
        form = RegistrationForm()

    return render(request, 'donation_boi/register.html', {'form': form})

def search(request):
    if request.method == "GET" and (request.GET.get("store", None) is not None or request.GET.get("item_category", None) is not None \
    or request.GET.get("item_name", None) is not None):
        try:
            store_id = request.GET.get("store", "")
        except:
            store_id = ""
        item_category = request.GET.get("item_category", "")
        item_name = request.GET.get("item_name", "")
        items = Item.objects.filter(category__icontains=item_category, name__icontains=item_name)
        print(store_id)
        if store_id != "":
            items = items.filter(store_id__exact=store_id)
        return render(request, "donation_boi/search.html", {'items': items})
    else:
        form = SearchStoresForm()

    return render(request, 'donation_boi/search.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("/")