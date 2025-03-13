from .models import Post
from .forms import NewPostForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home_page(request):
    autumn = Post.objects.all()
    return render(request, 'blog_app/index.html', {'posts': autumn})

def reading_posts(request, pk):
    specific_post = Post.objects.get(pk=pk)
    return render(request, 'blog_app/specific_post.html', {'specific_post': specific_post})

def deleting_posts(request, pk):
    specific_post = Post.objects.get(pk=pk)
    specific_post.delete()
    return redirect('home_page')

def updating_posts(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewPostForm(request.POST, instance=post)  # Bind form to the existing post instance
        if form.is_valid():
            form.save()  # Save the changes to the database
            return redirect('home_page')  # Redirect to a detail view or another page
    else:
        form = NewPostForm(instance=post)
    return render(request, 'blog_app/post.html', {'new_post_form': form})

def new_post(request):
    form = NewPostForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        # Create and save a new BlogPost instance
        blog_post = Post(title=title, content=content, user=author)
        blog_post.save()
        return redirect('home_page')
    return render(request, 'blog_app/post.html', {'new_post_form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'specific_post'
    template_name = 'blog_app/specific_post.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("home_page")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
