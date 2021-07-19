from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
          user = form.save()
          user.refresh_from_db()  # load the profile instance created by the signal request.FILES['Images']
          user.profile.profile_PIC = request.FILES['profile_PIC']
          user.profile.Full_Address = form.cleaned_data.get('address')
          user.profile.Category = form.cleaned_data.get('Category')
          user.profile.city = form.cleaned_data.get('city')
          user.profile.state = form.cleaned_data.get('state')
          user.profile.pincode = form.cleaned_data.get('pincode')
          user.save()
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=user.username, password=raw_password)
          login(request, user)
          return redirect('home')
    else:
      form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
