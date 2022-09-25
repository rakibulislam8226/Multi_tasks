from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views import View

class usersList(View):
    def get(self,request):
        users= get_user_model().objects.all()
        context = {
            'users':users
        }
        return render(request, 'usersList.html',context)

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            users_ids = request.POST.getlist('ids[]')

            for id in users_ids:
                user = User.objects.get(pk=id)
                send_mail(
                    'Mail From rakibkhan9065@gmail.com.com',
                    'Welcome to Django',
                    'rakibkhan9065@gmail.com',
                    [user.email],
                    fail_silently=False
                )
            return redirect('users')