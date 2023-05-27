from django.shortcuts import render, redirect
from .models import Post, Author
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

# This will allow a user to view the posts and also to search using keywords that could be cotained in the post
class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        context['count'] = context['posts'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search') or '' # The search method implemented
        if search_input:
            context['posts'] = context['posts'].filter(title_contains = search_input)
            context['search_input'] = search_input
        return context #note the word used posts and search_input: to be used in input submit value

# This allows a user to view the Post Details
class PostDetail(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name = '' # include the html file to show the details

#This allows a user to create a Post with title, content and a picture attached
class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'post_picture']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

# User is able to Update a post with this class
class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content', 'post_picture']
    success_url = reverse_lazy('post')

# User is able to Delete a Post with this class
class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('post')

#This will allow a user to login

class UserLoginView(LoginView):
    template_name = '' #add the path to the html file that allows a user to log in
    field = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('post') #successfully create a user return to the landing page of viewing posts
    
# This class will help us to register a user in the blog
class RegisterPage(FormView):
    template_name = '' #add the link to the html file that allows us to create a user/author
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('post') # redirects an autheniticated user to the home page if user is registered and authenticated

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, **kwargs)
