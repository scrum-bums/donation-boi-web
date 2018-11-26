from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import ListView
from django import forms
import json,datetime
from django.contrib.auth.models import User, Group # need to import Group from https://stackoverflow.com/a/6288863/5434744
import random, string
from .models import Store


# Create your views here.
class StoreList(ListView):
    model = Store
    context_object_name = "stores"