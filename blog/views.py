from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Post, Category, Comment
from accounts.forms import CommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context)

# singlePost


# class postDetailView(DetailView):
#     model = Post



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            messages.success(request, 'Profile details updated.')
            redirect('post-detail',kwargs={'pk':pk})
        else:
            pass
    context = {
        'object': post,
        'form': CommentForm(),
        'cats': Category.objects.all().order_by('-id')
    }
    return render(request, 'blog/post_detail.html', context)

class CategoryPostDetailView(DetailView):
    model = Category
    