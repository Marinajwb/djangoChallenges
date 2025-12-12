from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january"  : "Eat no meat for the entire month!",
    "fabruary" : "walk for at leat 20 minutes everyday",
    "march"    : "i love my cats" ,
    "april"    : "i love happy ",
    "may"      : "i love albam",
    "june"     : "i love my two cats" ,
    "july"     : "i love my life",
    "august"   : "i want to travel ",
    "september": None
}

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())
  return render(request, "challenges/index.html",
                {
                  "months" : months
                } )
  #"<li><a href="...">...</li><li>...</li><li>...</li>"
  
  reponse_data = f"<ul>{list_items}</ul>"
  
  """
    <ul>
        <li><a href="challenges/january">January</a></li>
    </ul>
  """
  return HttpResponse(reponse_data)

def monthly_number_challenge(req,month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
       return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
   try:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html",{
       "cats"         : challenge_text
     , "month_name"   : month
    })
   except:
    raise Http404()
    # response_data =  render_to_string("404.html") 
    #return  HttpResponseNotFound(response_data)  
    