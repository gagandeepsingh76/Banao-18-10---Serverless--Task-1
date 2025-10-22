from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import UserSignupForm, UserLoginForm
from .models import User


class SignupView(CreateView):
    """
    Class-based view for user signup
    """
    model = User
    form_class = UserSignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        """
        Handle successful form submission
        """
        response = super().form_valid(form)
        messages.success(
            self.request, 
            f'Account created successfully! Please login with your credentials.'
        )
        return response
    
    def form_invalid(self, form):
        """
        Handle form validation errors
        """
        messages.error(
            self.request, 
            'Please correct the errors below and try again.'
        )
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    """
    Custom login view extending Django's LoginView
    """
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        """
        Handle successful login and redirect based on user type
        """
        response = super().form_valid(form)
        user = self.request.user
        
        if user.user_type == 'patient':
            messages.success(self.request, f'Welcome, {user.first_name}!')
            return redirect('accounts:patient_dashboard')
        elif user.user_type == 'doctor':
            messages.success(self.request, f'Welcome, Dr. {user.last_name}!')
            return redirect('accounts:doctor_dashboard')
        
        return response
    
    def form_invalid(self, form):
        """
        Handle login errors
        """
        messages.error(
            self.request, 
            'Invalid username or password. Please try again.'
        )
        return super().form_invalid(form)


class PatientDashboardView(TemplateView):
    """
    Dashboard view for patients
    """
    template_name = 'accounts/patient_dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Ensure only patients can access this view
        """
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if request.user.user_type != 'patient':
            messages.error(request, 'Access denied. This area is for patients only.')
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        """
        Add user data to context
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class DoctorDashboardView(TemplateView):
    """
    Dashboard view for doctors
    """
    template_name = 'accounts/doctor_dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Ensure only doctors can access this view
        """
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if request.user.user_type != 'doctor':
            messages.error(request, 'Access denied. This area is for doctors only.')
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        """
        Add user data to context
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@login_required
def logout_view(request):
    """
    Logout view
    """
    from django.contrib.auth import logout
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('accounts:login')