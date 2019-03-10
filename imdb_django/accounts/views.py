from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST or None)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = user_form.save(commit=False)
            user.set_password(raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid password/username')
    else:
        user_form = UserForm()
    return render(request, 'accounts/register.html', {"form" : user_form})



def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("failed login !")
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    logout(request)
    return redirect('home')