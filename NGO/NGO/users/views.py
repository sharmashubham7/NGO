from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import admin_required


def home(request):
    return HttpResponse('You are now home!!')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login-page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_admin:
        return HttpResponse(f'you are on admin page {request.user.username}')

    else:
        return render(request, 'users/profile.html')


@login_required
@admin_required
def admin_view(request):
    return HttpResponse("Exclusive test admin page!!!!!!!!!")