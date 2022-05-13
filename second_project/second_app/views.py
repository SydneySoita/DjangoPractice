from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
from second_app.forms import My_Model_Form


# Create your views here.
def help(request):
    my_dict = {'insert_me': "Go to /users to sign up"}
    return render(request, 'second_app/help.html', context=my_dict)


# def user(request):
#     user_list = User.objects.order_by('firstname')
#     new_dict = {'user_records': user_list}
#     return render(request, 'second_app/users.html', context=new_dict)


def user(request):
    form = My_Model_Form()

    if request.method == "POST":
        form = My_Model_Form(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return help(request)
        else:
            print("INVALID FORM")
    return render(request, 'second_app/users.html', {'form': form})
