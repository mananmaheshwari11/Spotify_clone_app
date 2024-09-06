from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserLoginForm, CustomUserCreationForm 

# Create your views here.
def index(request):
    return render(request,'accounts/index.html')

def signup(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
        
def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not request.COOKIES.get('has_logged_in'):
                    response = redirect('/music/info')
                    response.set_cookie('has_logged_in', 'true', max_age=365*24*60*60)  # Cookie lasts for 1 year
                    return response
                else:
                    return redirect('/music/listen')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

