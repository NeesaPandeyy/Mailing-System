from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()


def home(request):
    return render(request,'dashboard/home.html')


@login_required
def dashboard(request):
    admins = User.objects.filter(role='admin') 
    current_user = request.user.role
    if current_user == 'admin':
        messages = Message.objects.all().order_by('-timestamp')
    else:
        messages = Message.objects.filter(sender=request.user).order_by('-timestamp')

    return render(request, 'dashboard/dashboard.html', {'admins': admins, 'messages': messages,'current_user':current_user})  # Pass messages to template

@login_required
def compose(request):
    admins = User.objects.filter(role='admin')  # Fetch all admins for dropdown

    if request.method == 'POST':
        to_email = request.POST.get('toEmail')
        subject = request.POST.get('subject')
        content = request.POST.get('message')

        try:
            recipient = User.objects.get(email=to_email)  # Get recipient by email
            Message.objects.create(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                content=content
            )
            return redirect('dashboard')  # Redirect to dashboard after sending
        except User.DoesNotExist:
            error_message = "Recipient not found. Please enter a valid admin email."
            return render(request, 'dashboard/dashboard.html', {'admins': admins, 'error': error_message})

    return render(request, 'dashboard/dashboard.html', {'admins': admins})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('user-login')
