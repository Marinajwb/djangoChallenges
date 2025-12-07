from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challenges = {
    "january"  : "Eat no meat for the entire month!",
    "fabruary" : "walk for at leat 20 minutes everyday",
    "march"    :  "i love my cats" ,
    "june"     :  "i love my two cats" 
}
def index(request):
    return HttpResponse("This works")

def february(request):
    return HttpResponse("work for at 20 minutes every ")

def march(request):
    return HttpResponse("i love my cat")

def monthly_number_challenge(req,month):
    months = list(monthly_challenges.keys())
    
    if month > len(month):
       return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-0]
    redirect_path = reverse("month-challenge",args=[redirect_month]) #challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
   try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
   except:
    return  HttpResponseNotFound("My cats are the best!!!!")  
    