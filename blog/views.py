from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post,Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def post_list_view(request):
    posts_list = Post.published.all()
    query = request.GET.get("q")
    if query:
        posts_list = posts_list.filter(
            Q(title__contains = query) |
            Q(body__contains = query)
        ).distinct()

    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post/detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post/add_comment_to_post.html', {'form': form})
# Create your views here.

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail_view', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail_view', pk=comment.post.pk)
