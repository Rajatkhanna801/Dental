from django.shortcuts import render
from Dental.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def email(request, *args, **kwargs):
    subject = 'Welcome to DataFlair'
    message = 'Hope you are enjoying your Django Tutorials'
    recepient = str(sub['Email'].value())
    send_mail(subject,
        message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'Test/suceess.html', {'recepient': recepient})
    return render(request, 'Test/index.html', {'form':sub})