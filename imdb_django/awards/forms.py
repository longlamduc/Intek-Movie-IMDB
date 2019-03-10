from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from awards.models import Award
from movies.models import Movie
from celebs.models import Celeb

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = ['name', 'kind']

class CelebAwardForm(ModelForm):
    celebs = ModelMultipleChoiceField(queryset=Celeb.objects.all(),
                                        widget=CheckboxSelectMultiple())
    class Meta:
        model = Award
        fields = ['name', 'celebs']

class MovieAwardForm(ModelForm):
    movies = ModelMultipleChoiceField(queryset=Movie.objects.all(),
                                        widget=CheckboxSelectMultiple())

    class Meta:
        model = Award
        fields = ['name', 'movies']
