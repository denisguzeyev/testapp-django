from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from .forms import NameForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class LoginView(TemplateView, View):
    template_name = 'users/login.html'
    
    def get(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get('username'), 
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user = authenticate(username=request.POST.get('username'), 
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('home')
#            return render(request, 'home')
        else:
            return redirect(request.POST.get('next', 'register'))


class LogoutView(View):
    def post(self, request, *args, **kwargs):
#        return redirect('home')
        logout(request)
        return redirect(request.POST.get('next', 'login'))


class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
#         return self.render_to_response({})
        return render(request, self.template_name, {'form': NameForm})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user = User.objects.create_user(request.POST.get('username'), 
									'user@mail.com', request.POST.get('password1'))
        user.is_staff=True
        user.save()
        return redirect('home')
       
