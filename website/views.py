from django.shortcuts import render
from django.core.mail import send_mail
from . import models
import re

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message'] + ' from ' + email
        tyn = 'Thank You!'
        errmsg = 'Please type in a valid email.'
        errmsg2 = 'Please don\'t leave blank message.'
        wrong_input = 'wrong'
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, email)):
            return render(request, 'contact.html', {'errmsg': errmsg, 'wrong_input': wrong_input})
        elif (len(message) <= 0):
            return render(request, 'contact.html', {'errmsg2': errmsg2, 'wrong_input': wrong_input})
        else:
            send_mail(subject, message, email, ['aierken.nadier@gmail.com'])
            return render(request, 'contact.html', {'tyn': tyn})

    else:
        return render(request, 'contact.html', {})

def project_index(request):
    return render(request, 'project_index.html', {})

def about(request):
    return render(request, 'about.html', {})