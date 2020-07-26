from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# from complaints.models import Complaints
# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    complains = user.complaints.all()
    return render(request,'account/dashboard.html',{'complains':complains})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
        # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
        # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
        # Save the User object
            new_user.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})



