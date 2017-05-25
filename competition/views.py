from django.shortcuts import render

import datetime

from .forms import SignUp

from .forms import Submission

from django.contrib import messages

from .models import Challenge

from .models import Participant

# Create your views here.

deadline = datetime.datetime(2017,5,22,05,00,00)
startofcomp = datetime.datetime(2017,5,24,10,00,00)
endofcomp = datetime.datetime(2017,5,25,10,00,00)


def default(request):
    return render(request, 'static/index.html', {})

def challengeslist(request):
     if datetime.datetime.now() > startofcomp: 
         posts = Challenge.objects.filter()
         return render(request, 'challengeslist.html', {'challenges': posts}) 
     else:           
         return render(request,'static/heythere.html')

def leaderlist(request):
     participants = Participant.objects.order_by('-totalpoints')
#     if datetime.datetime.now() < endofcomp:
     return render(request, 'leaderboard.html', {'participants': participants}) 
#    else:
#        return render(request,'static/heythere.html')
          
"""
def application(request):
    form = SignUp()
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            if datetime.datetime.now() < deadline:
                user = form.save()
                messages.success(request, 'You Have succesfully signed up! You will be messaged a UUID later so you can use it during the competition')
            else:
                messages.error(request,"The Application Proccess for the Competition has ended! Your Application won't be accepted the competition")
from .models import Participant
    else:
       form_class = SignUp
    return render(request, 'participantform.html', {'form':form})
"""

def application(request):
    return render(request, 'static/appsclosed.html')
def submitentry(request):
    form = Submission()
    if request.method == "POST":
        form = Submission(request.POST,request.FILES)
        if form.is_valid():
            if datetime.datetime.now() < endofcomp:
                user = form.save()
                messages.success(request, 'The Entry has been succesfully submitted! You can check the leaderboard')
            else:
                messages.error(request,"The Competition has ended! You can see the winners on the Leaderboard!")
    else:
       form_class = SignUp
    return render(request, 'entryform.html', {'form':form})
