from django.shortcuts import render
from django.http import HttpResponse
from MainPage.models import HomePageInfo
from django.contrib.auth.decorators import login_required
from django.core import serializers
from json import loads

# Load the homepage up with the informationt text from the database

def MainPage(request):
    raw_template_info = HomePageInfo.objects.all()
    serialized_info = loads(serializers.serialize("json", list(raw_template_info)))
    info = serialized_info[0]["fields"]
    return render(request, 'mainpage/HomePage.html', {"items": info})



# @login_required
def ChangeForm(request):
    # form = HomePageInfo(intro_text="I love to do web development and other fun stuff! \n This site was written in Python using Django v2.1.1")
    # form.save()
    if request.method == 'POST':
        print("Post request made!")
        return HttpResponse("Post request received!")
    return HttpResponse("HellO!")
