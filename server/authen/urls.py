from django.urls import path
from . import views
from django.contrib.auth import views as auth_views, logout
from .forms import loginForm, changePasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='authen/password_change.html', form_class= changePasswordForm, success_url='/dj/profile'), name='passwordchange'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('profile_edit/', views.ProfileEdit.as_view(), name='profile_edit'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='authen/login.html', authentication_form= loginForm), name='login'),
]