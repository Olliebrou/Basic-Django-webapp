from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewUserForm
from django.utils.http import url_has_allowed_host_and_scheme

# Create your views here.


def user_login(request):
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    nxt = request.POST.get('next', '')
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:user_login') + f'?next={nxt}'
        )
    else:
        login(request, user)
        if nxt and url_has_allowed_host_and_scheme(nxt, None):
            return redirect(nxt)
        else:
            return redirect('/')

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        nxt = request.POST.get('next', '')
        if form.is_valid():
            form.save()
            if nxt and url_has_allowed_host_and_scheme(nxt, None):
                return HttpResponseRedirect(reverse('user_auth:user_login') + f'?next={nxt}')
            else:
                return HttpResponseRedirect(reverse('user_auth:user_login'))
    else:
        nxt = request.GET.get('next', '')
        form = NewUserForm()
    return render(request, 'authentication/create_user.html', {'form': form, 'next':nxt})
