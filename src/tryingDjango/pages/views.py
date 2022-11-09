from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# You add HTML here

#Notes  in args we will see a request comming so we can directly import a request.

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    print(request.user)
    my_context={
        "my_text": "this is about us",
        "my_number": 1234321,
        "my_list": [123, 675, 4564, 7658]
    }

    # return HttpResponse("<h1> Hi This is our contacts page </h1>")
    return render(request, "about.html", my_context)