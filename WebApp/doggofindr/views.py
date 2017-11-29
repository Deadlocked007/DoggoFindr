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

def myPage(request):
    user = User.objects.get(username=request.user)
    imageList =[]
    imgs = Image.objects.all().order_by('-id')
    for i in imgs:
        if i.author == user:
            imageList.append(i)
    if request.method == 'POST':
        print("request is POST")
        images = request.FILES.getlist("files") #Get the file from HTML
        if len(images) > 0 :
            for count, x in enumerate(images):
                formImg = ImageForm(request.POST or None, request.FILES or None)#create new image using the Django Form
                new_img = formImg.save(commit=False) #Temporarily saving the new image but not in the database
                new_img.imgFile = x #Set the image file as the file uploaded
                new_img.author = request.user
                new_img.breedName = "Unknown"
                new_img.save() #Save the image in the database
                print(new_img.imgFile)
    user = request.user
    context = {
        "imgList" : imageList,
        "user": user,
    }
    return render(request, 'doggofindr/myPage.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return home(request)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
