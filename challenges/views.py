from ast import arg
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
monthly_challenge = {
    "january": "January Challenge",
    "february": "february Challenge",
    "march": "march Challenge",
    "april": "april Challenge",
    "may": "may Challenge",
    "june": "june Challenge",
    "july": "july Challenge",
    "august": "august Challenge",
    "september": "september Challenge",
    "october": "october Challenge",
    "november": "november Challenge",
    "december": "december Challenge",
}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())
    for month in months:
        month_path = reverse("monthly-challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month}</a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    forward_month = months[month-1]
    redirected_path = reverse("monthly-challenges", args=[forward_month])
    return HttpResponseRedirect(redirected_path)


def monthly_challenges(request, month):
    # challenge_text = "None"

    # if month == "january":
    #     challenge_text = "January Challenge"

    # elif month == "february":
    #     challenge_text = "February Challenge"

    # elif month == "march":
    #     challenge_text = "March Challenge"

    # else:
    #     return HttpResponseNotFound("Month currently not supported")

    # return HttpResponse(challenge_text)

    try:
        challenge_text = monthly_challenge[month]
    except:
        return HttpResponseNotFound("Month currently not supported")

    return HttpResponse(challenge_text)
