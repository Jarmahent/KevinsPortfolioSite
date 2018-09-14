from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from MainPage.models import HomePageInfo
from django.contrib.auth.decorators import login_required
from django.core import serializers
from json import loads
from MainPage.forms import HomePageModelForm
from pprint import pprint

# Load the homepage up with the informationt text from the database

def MainPage(request):
    raw_template_info = HomePageInfo.objects.all()
    serialized_info = loads(serializers.serialize("json", list(raw_template_info)))
    try:
        info = serialized_info[0]["fields"]
        pprint(info)
    except IndexError:
        info = {
        'intro_text': 'default',
        'project_five': 'default',
        'project_four': 'default',
        'project_one': 'default',
        'project_seven': 'default',
        'project_six': 'default',
        'project_three': 'default',
        'project_two': 'default'
    }
    # print(info)
    return render(request, 'mainpage/HomePage.html', {"items": info})



@login_required
def ChangeForm(request):
    if request.method == 'POST':

        form = HomePageModelForm(request.POST)
        if form.is_valid():
            HomePageInfo.objects.all().delete()
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')
    else:
        raw_template_info = HomePageInfo.objects.all()
        serialized_info = loads(serializers.serialize("json", list(raw_template_info)))
        try:
            info = serialized_info[0]["fields"]
        except IndexError:
            info = info = {
            'intro_text': 'default',
            'project_five': 'default',
            'project_four': 'default',
            'project_one': 'default',
            'project_seven': 'default',
            'project_six': 'default',
            'project_three': 'default',
            'project_two': 'default'
        }

        form = HomePageModelForm(initial=info)
        print(form.errors)
    return render(request, 'EditHomePage/EditHomePage.html', {"form": form})
