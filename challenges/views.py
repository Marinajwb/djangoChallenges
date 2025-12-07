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
  list_items = ""
  months = list(monthly_challenges.keys())
  
  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args = [month]) 
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
  
  #"<li><a href="...">...</li><li>...</li><li>...</li>"
  
  reponse_data = """
    <ul>
        <li><a href="challenges/january">January</a></li>
    </ul>
  """
  return HttpResponse()

def monthly_number_challenge(req,month):
    months = list(monthly_challenges.keys())
    
    if month > len(month):
       return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-0]
    redirect_path = reverse("month-challenge",args=[redirect_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
   try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
   except:
    return  HttpResponseNotFound("<h1>My cats are the best!!!!</h1>")  
    