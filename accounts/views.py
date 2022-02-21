from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:user_home")
    template_name = "create.html"

    # def post(self, request, *args, **kwargs):
    #     form = SignUpForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(email=email, password=password)
    #         login(request, user)
    #         return redirect('accounts:user_home')
    #     return render(request, 'create.html', {'form': form})
    #
    # def get(self, request, *args, **kwargs):
    #     form = SignUpForm(request.POST)
    #     return render(request, 'create.html', {'form': form})

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
# form_validでアカウントを作ったらそのままログインさせる


class Home(TemplateView):
    template_name = "home.html"


class UserHome(TemplateView):
    template_name = "user_home.html"
