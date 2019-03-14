from django.forms import ModelForm, ValidationError, ModelChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Movie
from category.models import Category
from celebs.models import Celeb

class MovieForm(ModelForm):
    category = ModelChoiceField(queryset=Category.objects.all())
    celebs = ModelMultipleChoiceField(queryset=Celeb.objects.all(),
                                        widget=CheckboxSelectMultiple())

    class Meta:
        model = Movie
        fields = '__all__'

    def check_name(self):
        title = self.cleaned_data.get('title')
        if Movie.objects.filter(title = title).count() != 0:
            self.errors['title'] = ['This movie existed']
            return False
        return True

    def embedTrailer(self):
        """ Convert the field 'trailer' that can be embed on the page """
        return self.cleaned_data.get('trailer').replace('watch?v=', 'embed/')
