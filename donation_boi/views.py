from django.shortcuts import render, redirect
from django.http import HttpResponse
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

def logout_view(request):
    logout(request)
    return redirect("/")