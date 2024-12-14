from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
   if request.user.is_anonymous:
      return redirect("/login")
   return render(request,'index.html')

def about(request):
   return render(request,'contact.html')

def sort(request):
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            element1 = int(request.POST.get('element1'))
            element2 = int(request.POST.get('element2'))
            element3 = int(request.POST.get('element3'))
            element4 = int(request.POST.get('element4'))
            elements = [element1, element2, element3, element4]
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

        # Perform selection sort and get the steps
        steps = selection_sort_steps(elements)
        # Render the template with the sorted steps
        return render(request, "sort.html", {'steps': steps})

    # Render the template for GET requests
    return render(request, "sort.html")

def selection_sort_steps(arr):
    steps = []  # Store each step of the array
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[j]= arr[i]
        arr[i] = arr[min_idx]
        # Record the array state before the swap
        steps.append(min_idx)  # Take a snapshot of the current state
        
        # Swap the found minimum element with the element at the current position
       

    return steps

 


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

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            login(request, user)  # Log the user in after successful registration
            return redirect('login')  # Replace 'home' with the name of your homepage view
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


