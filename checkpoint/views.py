from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django import forms
from checkpoint.models import image
from checkpoint.getdata import get_all_images, get_some_images
from datetime import datetime as dt
#from checkpoint.getdata import getdata, imagelink
#from checkpoint.forms import optionform

#image_list = imagelink #1. Define model/data as a list first
#image_dict = {'image': image_list} #2. Then put list into dictionary before can pass into template

# Grabbing images from models
#def index_view(request):
#
#    imageobj = image.objects.all() #put all images into list
#    context_dict = {'image': imageobj}
#    return render(request, 'checkpoint/index.html', context_dict)

# Grabbing images direct from API
def index_view(request):
    now_time = dt.now().time()
    now_minute = dt.now().minute

    if now_minute == 0 or now_minute == 15 or now_minute == 30 or now_minute < 45 :
        all_images = get_all_images() #stores jsondict
        some_images = get_some_images(all_images) #stores imagelink

    some_images = image.objects.all() #grab model data put into list
    context_dict = {'image': some_images}
    return render(request, 'checkpoint/index.html', context_dict)
