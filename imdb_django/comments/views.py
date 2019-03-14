from django.shortcuts import redirect
from .models import Comment
from movies.models import Movie

# Create your views here.
def add_comment(request, movie_id=None):
    if request.method == 'POST':
        content = request.POST.get('content')
        movie = Movie.objects.get(id=movie_id)
        username = request.user
        comment = Comment(content=content, movie=movie, username=username)
        comment.save()
        return redirect('movie_detail', movie_id)

def edit_comment(request, movie_id=None, comment_id=None):
    comment = Comment.objects.get(id=comment_id)
    comment.content = request.POST.get('content')
    comment.save()
    return redirect('movie_detail', movie_id)

def delete_comment(request, movie_id=None, comment_id=None):
    Comment.objects.get(id=comment_id).delete()
    return redirect('movie_detail', movie_id)
