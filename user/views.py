from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


# class Login(View):
#     def get(self, request):
#         form = LoginForm()
#         print(request.path)
#         return render(request, 'user/login.html', {'form': form})
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             my_user = authenticate(username=username, password=password)
#             if my_user is not None:
#                 login(request, my_user)
#                 return HttpResponseRedirect(reverse('polls:index'))
#         return render(request, 'user/login.html', {'form': form})


class Register(View):

    def get(self, request):
        abc = request.path
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password1')
            form.save()
            my_user = authenticate(username=username, password=password)
            login(request, my_user)
            return HttpResponseRedirect(reverse('polls:index'))
        return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()
        content = {
            'u_form': u_form,
            'p_form': p_form
        }
    return render(request, 'user/profile.html', content)
