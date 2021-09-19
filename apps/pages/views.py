from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    my_context = {
        "abc": 312,
        "example": "This is an example",
        "example_list": [1231,123423,242543,453243]
    }
    return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})
