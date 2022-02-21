from django.http import  HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:user_home")
    template_name = "create.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
# form_validでアカウントを作ったらそのままログインさせる


class Home(TemplateView):
    template_name = "home.html"


class UserHome(LoginRequiredMixin, TemplateView):
    template_name = "user_home.html"
