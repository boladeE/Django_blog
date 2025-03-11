from .models import Post
from .forms import NewPostForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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