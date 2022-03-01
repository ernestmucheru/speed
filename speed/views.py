from datetime import datetime
from django.shortcuts import render
import email
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,redirect
# from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime, timezone

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
    return render(request, 'base.html',{})

# def process_request(request):
#     #email function
#     #subject
#         subject = request.POST.get('subject')
#         #message
#         message = request.POST.get('message')
#         #From email
#         email = request.POST.get('email')

        

#     send_mail(data['subject'], message,'This is a test message body', ['estmuch254@gmail.com'])
#     return HttpResponseRedirect("/")