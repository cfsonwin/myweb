from django.http import HttpResponse
from django.shortcuts import render

from mymodel.models import Users


# Create your views here.
def index(request):
    # add_new_record("xiaozhu", 25, "13036836384")
    # delete_record(1)
    # update_record(2)
    respone = render(request, "mymodel/homepage.html", {})
    return HttpResponse(respone)


def add_new_record(name, age, phone):
    user = Users()
    user.name = name
    user.age = age
    user.phone = phone
    print("add new record %s" % name)
    user.save()


def delete_record(id):
    model = Users.objects
    user = model.get(id=id)
    user.delete()
    print(user.name)


def update_record(id, name, age, phone):
    user = Users.objects.get(id=id)
    user.name = name
    user.age = age
    user.phone = phone
    user.save()


def select_record(opt):
    # all
    model = Users.objects
    if opt == "all":
        ulist = model.all()
        output = ', '.join([q.name for q in ulist])
        print(output)
        for user in ulist:
            print(user.id, user.name)
    elif opt == "filter":
        # ulist = model.filter(name="xiaohe")
        ulist = model.filter(age__gt=20)
        for user in ulist:
            print(user.id, user.name, user.age)
    elif opt == "orderby":
        # ulist = model.filter(name="xiaohe")
        ulist = model.order_by("age")[:3]
        for user in ulist:
            print(user.id, user.name, user.age)

    pass


def show_table(request):
    # try:
    ulist = Users.objects.all()
    user_dic = {"userlist": ulist}
    return render(request, "mymodel/users/model.html", user_dic)

    # except:
    #     return HttpResponse("Not exist!")



def show_add_new_user(request):
    return render(request, "mymodel/users/show_add.html")



def add_new_user(request):
    try:
        add_new_record(request.POST['name'], request.POST['age'], request.POST['phone'])
        context = {"info": "Add Successfully!"}
    except:
        context = {"info": "Add Unsuccessfully!"}
    return render(request, "mymodel/users/add_success.html", context)



def del_user(request, uid=0):
    try:
        delete_record(uid)
        context = {"info": "Delete Successfully!"}
    except:
        context = {"info": "Delete Unsuccessfully!"}
    return render(request, "mymodel/users/add_success.html", context)



def show_update_user(request, uid=0):
    context = {"uid": uid}
    user = Users.objects.get(id=uid)
    context = {"user": user}
    return render(request, "mymodel/users/show_update.html", context)


def update_user(request):
    try:
        update_record(
            request.POST['id'],
            request.POST['name'],
            request.POST['age'],
            request.POST['phone'],
        )
        context = {"info": "Update Successfully!"}
    except:
        context = {"info": "Update Unsuccessfully!"}
    return render(request, "mymodel/users/add_success.html", context)
