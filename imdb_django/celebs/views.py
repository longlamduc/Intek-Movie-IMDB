from django.shortcuts import render, redirect, get_object_or_404
from .forms import CelebForm
from .models import Celeb

# Create your views here.
def celeb(request):
    return render(request, 'celebs/celeb.html', {'celeb_list': Celeb.objects.all()})

def celeb_detail(request, celeb_id):
    celeb = get_object_or_404(Celeb, id=celeb_id)
    return render(request, 'celebs/detail.html', {'celeb': celeb})

def add_celeb(request):
    if request.method == 'POST':
        form = CelebForm(request.POST)
        if form.is_valid():
            celeb = form.save(commit=False)
            celeb.save()
            return redirect('celeb')
    else:
        form = CelebForm()
    return render(request, 'celebs/celeb_form.html', {'form': form})

def edit_celeb(request, celeb_id=None):
    item = get_object_or_404(Celeb, id=celeb_id)
    form = CelebForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('celeb')
    return render(request, 'celebs/celeb_form.html', {'form': form})

def delete_celeb(request, celeb_id=None):
    Celeb.objects.get(id=celeb_id).delete()
    return redirect('celeb')
