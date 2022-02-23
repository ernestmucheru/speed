from django.shortcuts import render
import email
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,redirect
# from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}

        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'],message, '', ['estmuch254@gmail.com'])
        messages.success(request, "Thank you for contacting us. We will get back to you shortly.")
    return render(request, 'home.html',{})
