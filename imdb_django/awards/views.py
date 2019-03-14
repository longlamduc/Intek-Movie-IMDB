from django.shortcuts import render, redirect, get_object_or_404
from .forms import AwardForm, MovieAwardForm, CelebAwardForm
from .models import Award
from movies.models import Movie
from celebs.models import Celeb
# Create your views here.
def award(request):
    movies = Movie.objects.all()[:3]
    celebs = Celeb.objects.all()[:3]
    context = {
        'movies': movies,
        'celebs': celebs,
        'award_list': Award.objects.all()
    }
    return render(request, 'awards/award.html', context=context)

def award_detail(request, award_id):
    award = get_object_or_404(Award, id=award_id)
    return render(request, 'awards/detail.html', {'award': award})

def add_award(request):
    if request.method == 'POST':
        form = AwardForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            if Award.objects.filter(name=name).count() != 0:
                raise ValidationError('This award existed')
            award = form.save(commit=False)
            award.save()
            form.save_m2m()
            return redirect('award')
    else:
        form = AwardForm()
    return render(request, 'awards/award_form.html', {'form': form})

def edit_award(request, award_id=None):
    item = get_object_or_404(Award, id=award_id)
    if item.kind == 'Celeb':
        form = CelebAwardForm(request.POST or None, instance=item)
    else:
        form = MovieAwardForm(request.POST or None, instance=item)
    if form.is_valid():
        award = form.save(commit=False)
        award.save()
        form.save_m2m()
        return redirect('award')
    return render(request, 'awards/award_form.html', {'form': form,'edit': 1})

def delete_award(request, award_id=None):
    Award.objects.get(id=award_id).delete()
    return redirect('award')
