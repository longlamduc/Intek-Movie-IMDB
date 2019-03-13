from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment
from movies.models import Movie

# Create your views here.
def add_comment(request, movie_id=None):
    if request.method == 'POST':
        print(request.user)
        # form = CommentForm()
        # comment = request.POST.get('content')
        # comment.username = str(request.user)
        # comment.movie = Movie.objects.get(id=movie_id)
        # comment.save()
        content = request.POST.get('content')
        movie = Movie.objects.get(id=movie_id)
        username = request.user
        comment = Comment(content=content, movie=movie, username=username)
        comment.save()
        return redirect('movie_detail', movie_id)
    # else:
    #     comment_form = CommentForm()
    #     return redirect('movie_detail', movie_id)
    # return render(request, 'comments/comment_form.html', {'form': form})


def edit_comment(request, movie_id=None, comment_id=None):
    item = get_object_or_404(Comment, id=comment_id)
    form = CommentForm(request.POST or None, instance=item)
    if form.is_valid():
        movie = form.save(commit=False)
        movie.save()
        form.save_m2m()
        return redirect('movie_detail', movie_id)
    return render(request, 'comments/comment_form.html', {'form': form})

def delete_comment(request, movie_id=None, comment_id=None):
    Comment.objects.get(id=comment_id).delete()
    return redirect('movie_detail', movie_id)
