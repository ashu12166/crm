from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from models import Post
from .forms import PostForm


@login_required
def message(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'post_list.html', {'xyz': posts})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('message_board:list')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_detail(request, pk=None):
    print request, pk
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})