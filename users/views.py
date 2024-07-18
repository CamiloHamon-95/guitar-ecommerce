from django.shortcuts import render, redirect
from .forms import form_signup, form_login
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def view_signup(request):
    
    if request.method == 'POST':
        form = form_signup(request.POST, request.FILES)
        if form.is_valid():
            form.save_data()
            return redirect('users:login')
        return render(request, 'users/signup.html', {'form':form})
    else:
        form = form_signup()
    return render(request, 'users/signup.html', {'form':form})

def view_login(request):
    
    if request.method == 'POST':
        form = form_login(request.POST)
        if form.is_valid():
            myuser = authenticate(
                request=request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if myuser:
                login(
                    request,
                    myuser
                )
                return redirect('guitars:index')  
            else:
                return render(
                    request,
                    'users/login.html',
                    {'form':form_login(),'error':'Invalid username or password'}
                )
        return render(request, 'users/login.html', {'form':form_login()})
    else:
        form = form_login()
    return render(request, 'users/login.html', {'form':form})

@login_required(login_url='/users/login/')
def view_logout(request):
    logout(request=request)
    return redirect('users:login')

@login_required
def view_update_profile(request):
    return render(request, 'users/update_profile.html')