from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, request
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView, ListView, DeleteView, View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CreateBlogForm
from .models import CreateBlogModel
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class CreateBlogView(LoginRequiredMixin, CreateView):
    template_name = 'blog_create.html'
    form_class = CreateBlogForm
    # success_url = reverse_lazy('Blog:blog_list')

    def post(self, request, *args, **kwargs):
        # formのactionでusernameを取ろうとするとなぜかフォームがDBに追加されないので、POSTが送信されたらフォームをセーブするようにしている
        user1 = self.request.user.username
        # urlのusernameを取得するために、requestで取得している
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog:blog_list', user1)


class BlogListView(LoginRequiredMixin, ListView):
    template_name = 'blog_list.html'
    model = CreateBlogModel

    def UserBlog(request, **kwargs):
        object_list = CreateBlogModel.objects.all()
        return render(request, 'blog_list.html', {'object_list': object_list})


class BlogDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog_detail.html'
    model = CreateBlogModel


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog_update.html'
    model = CreateBlogModel
    fields = ('blog_title', 'text')
    success_url = reverse_lazy('Blog:blog_list')

    def form_valid(self, form):
        user1 = self.request.user.username
        blog = form.save(commit=False)
        blog.updated_date = now()
        blog.save()
        return redirect('Blog:blog_list', user1)


@login_required
def delete_memo(request, pk):
    user1 = request.user.username
    blog = get_object_or_404(CreateBlogModel, id=pk)
    blog.delete()
    return redirect('Blog:blog_list', user1)
# URLに飛んだ時点で削除が実行され、blog_listにリダイレクトされる



