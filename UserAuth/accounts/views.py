# from django.shortcuts import render, redirect
# from accounts.models import User
# from accounts.form import UserRegistrationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate,login,logout


# def register(request):
#     form = UserRegistrationForm()
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration successful!')
#             return redirect('/login')
#         else:
#             messages.error(request, 'Registration failed!')
#     return render(request, 'accounts/register.html', {'form': form})

# def profile(request):
#     users=User.objects.all()
#     print("profile")
#     return render(request, 'accounts/profile.html',{'users': users})


# def login_page(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         print(name)
#         pswd = request.POST.get('password')
#         print(pswd)
#         user = authenticate(username=name, password1=pswd)
#         if user :
#             login(request, user)
#             messages.success(request, 'Login successful 👍!')
#             print("login success")
#             return redirect('/profile')
        
#         else:
#             messages.error(request, 'Please enter the correct username and password 🙂!')
#     return render(request, 'accounts/login.html')

# def logout_page(request):
#     if request.user.is_authenticated:
#         logout(request)
#         messages.success(request, 'Logged out successfully 👋!')
#     return redirect('/login')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .form import RegisterForm

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('profile')
#     return render(request, 'accounts/login.html')

def login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            error_message = "Invalid username or password."

    return render(request, 'accounts/login.html', {'error_message': error_message})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    return redirect('login')
