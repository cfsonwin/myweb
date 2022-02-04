from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return render(request, "myview/index.html")


def resp01(request):
    return HttpResponse("resp01")


def resp404(request):
    return HttpResponseNotFound("page not found")
    # return HttpResponse(status=403)
    # raise Http404

# urls redirection
def respred(request):
    # 1, use path name
    return redirect(reverse('mindex'))