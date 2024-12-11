from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
   if request.user.is_anonymous:
      return redirect("/login")
   return render(request,'index.html')

def loginuser(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username = username, password = password)
      if user is not None:
         login(request,user)
         return redirect("/")

      else:  
         return render(request,'login.html')
         
   return render(request,'login.html')

def logoutuser(request):
   logout(request)
   return redirect("/login")


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('login.html')  # Replace 'home' with the name of your homepage view
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index.html')  # Redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

