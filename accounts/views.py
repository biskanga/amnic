from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        phonenumber = request.POST.get('phone_number')
        address = request.POST.get('address')

        if len(password1) < 8:
            messages.info(request, 'password cannot be less than 8 characters')
            return redirect('signup')
        elif password1 != password2:
            messages.info(request, 'Passwords do not match. Please check')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Sorry this username has already been taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Sorry this email has already been used')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
            user.save()
                
            profile = Profile(state=state, gender=gender, phone_number=phonenumber, address=address)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        return render(request, 'accounts/signup.html')        
    


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'invalid login credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login')
def profile_view(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    auth.logout(request)
    return redirect('login')