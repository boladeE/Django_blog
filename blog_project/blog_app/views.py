from django.shortcuts import render
from .models import Post

def home_page(request):
    autumn = Post.objects.all()
    return render(request, 'blog_app/index.html', {'posts': autumn})

def user_input(request):
    if request.method == 'POST':
        print(request.POST.get('Input 1'))
        print(request.POST.get('Input 2'))
    return render(request, 'blog_app/user_input.html')
# Create your views here.
