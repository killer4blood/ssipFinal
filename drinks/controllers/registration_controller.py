from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings



def index(request):
    msg = ''
    if request.method == 'POST':
        req = request.POST.dict()
        username = req['username']
        password = req['password']
        email = req['email']
        try:
            user = User.objects.get(username=username)
            msg = 'Username or E-Mail is already Registered'
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.save()
            msg = ''
            send_mail(
                'Splash: Registration Successful',
                'You are now an official member of Splash Drink Corner! You can now order custom drinks.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
        return HttpResponseRedirect('/accounts/login/')
    data = {
        'user_exists_error': msg,
    }
    return render(request, 'registration.html', data)

