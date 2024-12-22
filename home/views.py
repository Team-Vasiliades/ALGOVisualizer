from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import CustomUser # Use CustomUser if you have extended User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import translation
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import activate
import base64
# Create your views here.
# views.py
# views.py

def set_language(request):
    user_language = request.GET.get('lang', 'en')  # Default to 'en' if no language is selected
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the previous page or homepage


def set_language(request):
    user_language = request.GET.get('lang', 'en')  # Default to 'en' if no language is selected
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the previous page or homepage

def index(request):
   if request.user.is_anonymous:
    return render(request,'index.html')

def about(request):
   return render(request,'contact.html')

def selection_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "selection_sort.html", {
        'elements': elements,
    })

def selection_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    type = None
    order = None
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
            type = request.POST.get('algorithm')
            order = request.POST.get('order')
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "selection_sort.html", {
        'elements': elements,
        'type': type,
        'order': order
    })
def bubble_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    type = None
    order = None
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
            type = request.POST.get('algorithm')
            order = request.POST.get('order')
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "bubble_sort.html", {
        'elements': elements,
        'type': type,
        'order': order
    })
def insertion_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    type = None
    order = None
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
            type = request.POST.get('algorithm')
            order = request.POST.get('order')
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "insertion_sort.html", {
        'elements': elements,
        'type': type,
        'order': order
    })
def merge_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    type = None
    order = None
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
            type = request.POST.get('algorithm')
            order = request.POST.get('order')
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "merge_sort.html", {
        'elements': elements,
        'type': type,
        'order': order
    })
def quick_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    type = None
    order = None
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
            type = request.POST.get('algorithm')
            order = request.POST.get('order')
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "quick_sort.html", {
        'elements': elements,
        'type': type,
        'order': order
    })
def heap_sort(request):
    # Initialize elements to an empty list in case of GET request or invalid input
    elements = []
    type = None
    order = None
    
    if request.method == "POST":
        try:
            # Retrieve and convert the input values to integers
            elements = [
                int(request.POST.get('element0')),
                int(request.POST.get('element1')),
                int(request.POST.get('element2')),
                int(request.POST.get('element3')),
                int(request.POST.get('element4')),
                int(request.POST.get('element5')),
                int(request.POST.get('element6')),
                int(request.POST.get('element7')),
                int(request.POST.get('element8')),
                int(request.POST.get('element9'))
            ]
            type = request.POST.get('algorithm')
            order = request.POST.get('order')
        except (ValueError, TypeError):
            # Handle invalid input (non-integer values)
            elements = []

    # Return the rendered page with the elements and algorithm/order
    return render(request, "heap_sort.html", {
        'elements': elements,
        'type': type,
        'order': order
    })
def insdel(request):
   if request.method == "POST":
       value= request.POST.get('value')
       position= request.POST.get('position')
       elements= request.POST.getlist('elements')
       length= len(elements)
       return render(request, "insdel.html",{
            'length': length,
            'elements': elements,
            'value': value,
            'position': position
        })
   return render(request,'insdel.html')


# Stack implementation
class Stack:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size
        
    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            return "Stack is full"

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def top(self):
        if self.items:
            return self.items[-1]
        return None

    def get_stack(self):
        return self.items


stack = Stack()

def stack_visualizer(request):
    if request.method == "POST":
        operation = request.POST.get("operation")
        value = request.POST.get("value")

        if operation == "push" and value:
            error_message = stack.push(value)
            if error_message:
                messages.error(request, error_message)  # Store error message in session
        elif operation == "pop":
            popped = stack.pop()
            if not popped:
                messages.error(request, "Stack is empty, cannot pop!")
        elif operation == "top":
            top_element = stack.top()
            if top_element:
                messages.info(request, f"Top element is: {top_element}")
            else:
                messages.error(request, "Stack is empty, no top element!")

        # Redirect to prevent form resubmission
        return redirect('stack_visualizer')

    # Render the page for GET requests
    return render(request, "stack_visualizer.html", {
        "stack": stack.get_stack(),
    })
    
# Queue Implementation
class Queue:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            return "Queue is full"

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

    def get_queue(self):
        return self.items

# Deque Implementation
class Deque:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def add_front(self, item):
        if len(self.items) < self.max_size:
            self.items.insert(0, item)
        else:
            return "Deque is full"

    def add_rear(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            return "Deque is full"

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def get_deque(self):
        return self.items

# Circular Queue Implementation
class CircularQueue:
    def __init__(self, max_size=5):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            return "Queue is full"
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        removed_item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return removed_item

    def get_queue(self):
        return self.queue

queue = Queue()
deque = Deque()
circular_queue = CircularQueue()

@csrf_exempt
def queue_visualizer(request):
    selected_structure = request.GET.get("structure", "queue")
    context = {
        "selected_structure": selected_structure,
        "queue": queue.get_queue(),
        "deque": deque.get_deque(),
        "circular_queue": circular_queue.get_queue(),
        "front": circular_queue.front,
        "rear": circular_queue.rear,
    }

    if request.method == "POST":
        operation = request.POST.get("operation")
        value = request.POST.get("value")

        if selected_structure == "queue":
            if operation == "enqueue" and value:
                message = queue.enqueue(value)
                if message:
                    context["error"] = message
            elif operation == "dequeue":
                queue.dequeue()

        elif selected_structure == "deque":
            if operation == "add_front" and value:
                message = deque.add_front(value)
                if message:
                    context["error"] = message
            elif operation == "add_rear" and value:
                message = deque.add_rear(value)
                if message:
                    context["error"] = message
            elif operation == "remove_front":
                deque.remove_front()
            elif operation == "remove_rear":
                deque.remove_rear()

        elif selected_structure == "circular_queue":
            if operation == "enqueue" and value:
                message = circular_queue.enqueue(value)
                if message:
                    context["error"] = message
            elif operation == "dequeue":
                circular_queue.dequeue()

        # Redirect to clear POST data and avoid re-submission on refresh
        return redirect(f"./?structure={selected_structure}")

    return render(request, "queue_visualizer.html", context)
# Create your views here.
def index(request):
    # Check for the 'lang' parameter in the URL
    lang = request.GET.get('lang', 'en')  # Default to 'en' if no lang is selected
    activate(lang)  # Activate the selected language
    user = request.user
    profile_photo_base64 = None
    if request.user.is_anonymous:
     return render(request,'index.html')

    if user.profile_photo:
        # Convert binary to base64
        profile_photo_base64 = base64.b64encode(user.profile_photo).decode('utf-8')
    return render(request, 'index.html', {'profile_photo_base64': profile_photo_base64})



def logoutuser(request):
   logout(request)
   return redirect("/login")



def register(request):
    if request.method == "POST":
        # Get form data
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        profile_photo = request.FILES.get("profile_photo")  # Optional

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        # Save user to the database
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password),  # Hash password
            profile_photo=profile_photo.read()
        )



        # Redirect to login page with a success message
        messages.success(request, "Registration successful!")
        return redirect("home")

    return render(request, "register.html")




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    user = request.user
    profile_photo_base64 = None

    if user.profile_photo:
        # Convert binary to base64
        profile_photo_base64 = base64.b64encode(user.profile_photo).decode('utf-8')
    return render(request, 'profile.html', {'profile_photo_base64': profile_photo_base64})



def csrf_failure(request, reason=""):
    return redirect('home')  # 'index' is the name of your home page URL pattern


@login_required
def edit_profile(request):
    user = request.user  # Get the logged-in user

    if request.method == 'POST':
        # Update other fields
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.phone_no = request.POST.get('phone_no', user.phone_no)
        user.email = request.POST.get('email', user.email)
        user.username = request.POST.get('username', user.username)
        user.bio = request.POST.get('bio', user.bio)
        user.institute = request.POST.get('institute', user.institute)

        # Handle uploaded profile photo
        if 'profile_photo' in request.FILES:  # Check for 'profile_photo', not 'user.profile_photo'
            profile_photo_file = request.FILES['profile_photo']
            user.profile_photo = profile_photo_file.read()  # Save the uploaded file as binary data

        # Save user details
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Redirect to the profile page

    profile_photo_base64 = None
    if user.profile_photo:
        # Convert binary to base64 for display
        profile_photo_base64 = base64.b64encode(user.profile_photo).decode('utf-8')

    return render(request, 'edit.html', {'user': user, 'profile_photo_base64': profile_photo_base64})
