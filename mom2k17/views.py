from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Info , Register, School

from .models import Info
from django.views.generic.edit import CreateView


# Create your views here.
# def index(request):
#     return render(request, 'mom2k17/index.html')


def home(request):
    return render(request, 'mom2k17/home.html',{'title': 'home | MOM2k17'})

def about(request):
    return render(request, 'mom2k17/About.html',{'title': 'about | MOM2k17'})

def events(request):
    return render(request, 'mom2k17/Events.html',{'title': 'events | MOM2k17'})

def appcorner(request):
    return render(request, 'mom2k17/AppsCorner.html',{'title': 'appcorner | MOM2k17'})

def brainwave(request):
    return render(request, 'mom2k17/BrainWave.html',{'title': 'brainwave | MOM2k17'})

def expressions(request):
    return render(request, 'mom2k17/Expressions.html',{'title': 'expressions | MOM2k17'})

def flash(request):
    return render(request, 'mom2k17/Flash.html',{'title': 'flash | MOM2k17'})

def hospi(request):
    return render(request, 'mom2k17/Hospitality.html',{'title': 'hospitality | MOM2k17'})

def osd(request):
    return render(request, 'mom2k17/OnSpotDrawing.html',{'title': 'creations | MOM2k17'})


def quiz(request):
    return render(request, 'mom2k17/Quiz.html',{'title': 'quiz | MOM2k17'})

def sponsors(request):
    return render(request, 'mom2k17/Sponsors.html',{'title': 'sponsors | MOM2k17'})

def team(request):
    return render(request, 'mom2k17/Team.html',{'title': 'team | MOM2k17'})

def tme(request):
    return render(request, 'mom2k17/tme.html',{'title': 'tme | MOM2k17'})

def message(request):
    return render(request, 'mom2k17/message.html',{'title': 'message | MOM2k17'})

def workshop(request):
    return render(request, 'mom2k17/workshop.html.',{'title': 'workshop | MOM2k17'})



# def register(request):
#
#     if request.method == 'POST':
#         form = Register(request.POST)
#
#
#
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             city = form.cleaned_data['city']
#             address = form.cleaned_data['event']
#             phone_number = form.cleaned_data['phone_number']
#             institute = form.cleaned_data['institute']
#             event = form.cleaned_data['institute']
#             message = form.cleaned_data['message']
#
#
#
#             reg_obj = Register(name=name, email=email, city=city, address=address, phone_number=phone_number, institute=institute, event=event, message=message )
#
#             try:
#                 temp=Register.objects.get(name=name)
#             except :
#                 temp=False
#
#
#             if temp:
#                 return render(request, 'mom2k17/home.html', {'message': 'Already register'})
#
#             else:
#                 # reg_obj.momid='MOM2K17-'+str(reg_obj.pk)
#                 reg_obj.save()
#                 return render(request, 'mom2k17/home.html', {'message': 'YOUR MOM ID IS:'})
#
#
#         else:
#             form=Register()
#         return render(request, 'mom2k17/home.html',{'message':'Invalid email'})


class register(CreateView):
    model = Register

    fields = ['name', 'email', 'city', 'address', 'phone_number', 'institute', 'event', 'message']






# def subscribeView(request):
#     if request.method == 'POST':
#
#         form = Subscribe(request.POST)
#
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             info_obj = Info(email=email)
#             try:
#                 temp=Info.objects.get(email=email)
#             except :
#                 temp=False
#
#
#             if temp:
#                 return render(request, 'mom2k17/home.html', {'message': 'Already subscribed'})
#
#             else:
#                 info_obj.save()
#                 return render(request, 'mom2k17/home.html', {'message': 'You are now subscribed'})
#
#
#         else:
#             form=Subscribe()
#         return render(request, 'mom2k17/home.html',{'message':'Invalid email'})
