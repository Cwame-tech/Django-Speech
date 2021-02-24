from django.shortcuts import render
from django.http import HttpResponse
from .models import Speech
# Create your views here.


def home(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request,'speech/home.html',context)

def about(request):
    return render(request, 'speech/about.html',{'title':'about'})