from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm
from app.models import CustomUser
from django.contrib.auth import logout, login

def signup(request):
    form = SignupForm(instance=CustomUser())
    if request.method == 'POST':
        user = SignupForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('account_login')
    return render(request, 'allauth/base.html', context={'form': form})
  
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try : 
            user = CustomUser.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
        except:
            form = LoginForm(initial={'username': request.POST.get('username')})
            erreur = "Le nom d'utillisateur ou le mot de passe est incorrecte"
            return render(request, 'allauth/base.html', context={'form': form, 'erreur': erreur})
        if user is not None:
            login(request, user)
            return redirect('app-profile', user_id=user.id)
    return render(request, 'allauth/base.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('app-home')