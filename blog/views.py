from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Post, Category, Comment
from accounts.forms import CommentForm


def home(request):
    context = {
        'posts': Post.objects.all(),
        'navs': Category.objects.all()
    }
    return render(request, 'index.html', context)


def category_post_list(request, pk):
    context = {
        'cat': Category.objects.get(id=pk),
        'navs': Category.objects.all()

    }
    return render(request, 'blog/category.html', context)
# singlePost


# class postDetailView(DetailView):
#     model = Post


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.view += 1
    post.save()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            messages.success(
                request, 'Comment added...Your comment will appear after proper verification.. Thnaks..')
            # redirect('post-detail',kwargs={'pk':post.pk})
        else:
            pass
    context = {
        'object': post,
        'form': CommentForm(),
        'navs': Category.objects.all(),
        'cats': Category.objects.all().order_by('-id'),
        'popular_posts': Post.objects.filter(view__gte=4).order_by('-id')[:6]
    }
    return render(request, 'blog/post_detail.html', context)


class CategoryPostDetailView(DetailView):
    model = Category
