from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("This works")

def february(request):
    return HttpResponse("work for at 20 minutes every ")

def march(request):
    return HttpResponse("i love my cat")

def monthly_number_challenge(req,month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire life!!"
    elif month == "february":
        challenge_text = "walk for ay leat 20 minute everyday"
    elif month == "march":
        challenge_text = "i love my cats" 
    else:
        return HttpResponseNotFound("This month is not supported! 그리고 우리집 고양이는 귀여워용ㅎㅎ")
    return HttpResponse(challenge_text)