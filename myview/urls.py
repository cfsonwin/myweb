from django.contrib import admin
from django.urls import path
from myview.views import *

urlpatterns = [
    path('', index, name='mv_index'),
    path('resp01', resp01, name='mv_resp01'),
    path('resp404', resp404, name='mv_resp404'),
    path('respred', respred, name='mv_respred'),

]