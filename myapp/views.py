# from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    # reverse urls according to route name
    print(reverse("mredirection"))
    print(reverse("madd", args=('a')))
    return HttpResponse('hallo world')


def add(request, a):
    return HttpResponse('adding %s...' % a)


def find(request, a):
    return HttpResponse('finding %s...' % a)


def update(request, yy):
    return HttpResponse('updating in year %s...' % yy)


def raise_error(request):
    raise Http404('Webpage not exist!')


def redirection(request):
    return HttpResponseRedirect(reverse("mindex"))
