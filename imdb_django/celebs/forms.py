from django.forms import ModelForm, ValidationError, ModelChoiceField
from .models import Celeb


class CelebForm(ModelForm):
    class Meta:
        model = Celeb
        fields = '__all__'
