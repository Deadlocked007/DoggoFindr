from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Image
from.forms import ImageForm

def home(request):
    imgs = Image.objects.all().order_by('-id')
    user = request.user
    context = {
        "imgList" : imgs,
        "user": user,
    }
    return render(request, 'doggofindr/index.html',context)

def about(request):
    return render(request,'doggofindr/about.html')
