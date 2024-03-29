from django.shortcuts import render, redirect, get_object_or_404
from .forms import CelebForm
from .models import Celeb
from movies.models import Movie
from awards.models import Award
# Create your views here.
def celeb(request):
    movies = Movie.objects.all()[:3]
    celebs = Celeb.objects.all()[:3]
    context = {
        'movies': movies,
        'celebs': celebs,
        'celeb_list': Celeb.objects.all()
    }
    return render(request, 'celebs/index.html', context=context)

def celeb_detail(request, celeb_id=None):
    celeb = get_object_or_404(Celeb, id=celeb_id)
    return render(request, 'celebs/detail.html', {'celeb': celeb})

def add_celeb(request):
    if request.method == 'POST':
        form = CelebForm(request.POST)
        if form.is_valid() and form.check_name():
            celeb = form.save(commit=False)
            if celeb.avatar == "" or celeb.avatar == 'None':
                celeb.avatar = "https://znews-photo.zadn.vn/w660/Uploaded/wyhktpu/2018_11_22/TRI_1998.jpg"
            celeb.save()
            return redirect('celeb')
    else:
        form = CelebForm()
    return render(request, 'celebs/form.html', {'form': form})

def edit_celeb(request, celeb_id=None):
    item = get_object_or_404(Celeb, id=celeb_id)
    form = CelebForm(request.POST or None, instance=item)
    if form.is_valid():
        celeb = form.save(commit=False)
        if celeb.avatar == "" or celeb.avatar == 'None':
            celeb.avatar = "https://znews-photo.zadn.vn/w660/Uploaded/wyhktpu/2018_11_22/TRI_1998.jpg"
        celeb.save()
        return redirect('celeb')
    return render(request, 'celebs/form.html', {'form': form})

def delete_celeb(request, celeb_id=None):
    Celeb.objects.get(id=celeb_id).delete()
    return redirect('celeb')
