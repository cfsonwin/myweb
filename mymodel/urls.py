from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='my_model'),
    path('users', views.show_table, name="mshow_table"),
    path('users/addshow', views.show_add_new_user, name="mshow_add_new_user"),
    path('users/add', views.add_new_user, name="madd_new_user"),
    path('users/del/<int:uid>', views.del_user, name="mdel_user"),
    path('users/updateshow/<int:uid>', views.show_update_user, name="mshow_update_user"),
    path('users/update', views.update_user, name="mupdate_user"),

]