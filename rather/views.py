from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django import forms
from rather.models import option
from rather.forms import optionform

# Create your views here.

def index_view(request):
#    context = {'latest_question_list': latest_question_list}

#filter & order_by - Publisher.objects.filter(country="U.S.A.").order_by("-name")
#fiter & update - Publisher.objects.filter(id=52).update(name='Apress Publishing')
#    listeveything = option.objects.all()

    listeveything = option.objects.order_by('?')
    passthru = listeveything.first()
    return render(request, 'rather/index.html', {'passthru':passthru})

def thanks_view(request):
    return render(request, 'rather/thanks.html')

def input_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = optionform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            theme = request.POST.get('theme','')
            option1_text = request.POST.get('option1_text','')
            option2_text = request.POST.get('option2_text','')
            option_obj = option(theme = theme, option1_text = option1_text, option2_text = option2_text)
            option_obj.save()

            return HttpResponseRedirect('/rather/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = optionform()

    return render(request, 'rather/input.html', {'forms': forms})

#def inputview(input1, input2):
#    html = "Would you rather %s or %s"
#    return HttpResponse(html)
