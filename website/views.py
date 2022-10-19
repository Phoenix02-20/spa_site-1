from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def index(request):
    return render(request, "index.html", {})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send an email
        send_mail(
            'message from ' + name, #subject
            message, # message
            email, #from email
            ['priyarohitsharma20@gmail.com'], #to Email
        )

        return render(request, 'contact.html', {'name':name})
    else:
        return render(request, 'contact.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
