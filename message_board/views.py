from django.shortcuts import render
from models import Post

def message(request):
    posts = Post.objects.all()
    import pdb
    pdb.set_trace()
    return render(request, 'post_list.html', {'xyz': posts})


# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
