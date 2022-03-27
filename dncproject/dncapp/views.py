from django.shortcuts import redirect, render
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Article, Post

# Create your views here.

# def hello(request):
#     context = {}

#     login_session = request.session.get('login_session', '')

#     if login_session == '':
#         context['login_session'] = False
#     else:
#         context['login_session'] = True
#         return render(request, 'dncapp/index.html', context)

def index(request):
    context = {}

    login_session = request.session.get('login_session', '')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    if request.method == 'POST':
        post = Post()
        post.day = request.POST['day']
        post.cookname = request.POST['cookname']
        post.save()

        return redirect('index')
        
    else:
        post = Post.objects.all()
        context['post'] = post
    return render(request, 'dncapp/index.html', context)



class AuthorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        """Making sure that only authors can update, delete articles"""

        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseForbidden()
        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)

class ArticleList(ListView):
    model = Article
    paginate_by = 5
    ordering = ['-id']

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    success_url = reverse_lazy('index')
    field = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetail(DetailView):
    model = Article

class ArticleUpdate(AuthorRequiredMixin, UpdateView):
    model = Article
    field = ('title', 'content')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDelete(AuthorRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('index')