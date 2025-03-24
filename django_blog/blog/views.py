from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home page (or wherever)
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
