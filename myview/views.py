import os
from datetime import datetime
from myweb.settings import BASE_DIR
import folium
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def index(request):
    hash_now = hash(str(datetime.now()))
    context = {"hash_now": hash_now}
    return render(request, "myview/index.html", context)


def resp01(request):
    return HttpResponse("resp01")


def resp404(request):
    return HttpResponseNotFound("page not found")
    # return HttpResponse(status=403)
    # raise Http404


# urls redirection
def respred(request):
    # 1, use path name
    return redirect(reverse('my_model'))
    # return HttpResponse('<script>alert("Jump into user info"); location.href="/mymodel";</script>')


def map_plot(request, hash_now):
    url = "myview/map%s.html" % hash_now
    marker_list = [49.867, 8.6538]
    map_generate(url, marker_list, 13)
    return render(request, url)


def map_generate(url, marker_list, zoom_value):
    m = folium.Map(location=[49.867, 8.6538], zoom_start=zoom_value)
    tooltip = "Click me!"
    folium.Marker(
        marker_list, popup=folium.Popup("point in Darmstadt"), tooltip=tooltip
    ).add_to(m)
    # folium.Marker(
    #     [49.867, 8.6538], popup="<i>point in Darmstadt</i>", tooltip=tooltip
    # ).add_to(m)
    save_path = os.path.join(BASE_DIR, "templates/%s" % url)
    m.save(save_path)


from django.views import View


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("rewrite view class")
