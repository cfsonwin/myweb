from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='mindex'),
    path('add/<str:a>', views.add, name='madd'),
    path('find<int:a>', views.find, name='mfind'),
    re_path(r'^updating(?P<yy>[0-9]{4})$', views.update, name='mupdate'),
    path('redirection', views.redirection, name='mredirection'),
]