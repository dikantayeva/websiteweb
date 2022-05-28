from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'auth/login.html', {
                    'error': 'Incorrect Username or Password'
                })
        else:
            return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')