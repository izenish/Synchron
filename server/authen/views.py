from django.contrib.auth.decorators import login_required
from .forms import registrationForm, ProfileEditForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from .models import roles
from django.contrib import messages
from team.models import Team
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

class Registration(View):
    '''
        Registration form for user.
        Used a custom template rather than using a buildin template.
    '''
    def get(self, request):
        form = registrationForm()
        return render(request, 'authen/registration.html', {'form': form})
        
    @csrf_exempt
    def post(self, request):
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            '''
                Login the user after registration.
            '''
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')
        return render(request, 'authen/registration.html', {'form': form})

def home(request):
    return render(request, 'authen/home.html')

@login_required
def profile(request):
    '''
        Extract data for Profile page for user.
    '''
    user_info=User.objects.get(username=request.user)
    user_role= roles.objects.get(user=user_info)
    if user_role.role == 'sm':
        return render(request, 'authen/profile.html',{'user_role':user_role,'user_info':user_info})
    elif user_role.role == 'dev':
        # user_team=Team.objects.get(users=user_info)
        return render(request, 'authen/profile.html', {'user_info': user_info, 'user_role': user_role})

@method_decorator(login_required, name='dispatch')
class ProfileEdit(View):
    def get(self,request):
        form= ProfileEditForm(instance=request.user)
        return render(request, 'authen/profile_edit.html', {'form': form})
    def post(self,request):
        user=request.user
        form= ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.save()
            messages.success(request, 'Profile updated successfully')
        return render(request, 'authen/profile_edit.html', {'form': form})
        

# Create your views here.
