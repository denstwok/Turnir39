from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'teambio/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('teamprofile')
            except IntegrityError:
                return render(request, 'teambio/signupuser.html', {'form':UserCreationForm(), 'error':'Название команды уже занято'})
        else:
            return render(request, 'teambio/signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})
def teamprofile(request):
    return render(request, 'teambio/teamprofile.html')
