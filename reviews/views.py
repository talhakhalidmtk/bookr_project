from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world"
    # return HttpResponse("Hello, {}!".format(name))
    return render(request, 'base.html', {"name": name})


def search(request):
    search = request.GET.get("search", None)
    # return HttpResponse("Hello, {}!".format(name))
    return render(request, 'search.html', {"search": search})
