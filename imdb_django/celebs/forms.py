from django.forms import ModelForm
from .models import Celeb


class CelebForm(ModelForm):
    class Meta:
        model = Celeb
        fields = '__all__'

    def check_name(self):
      f = self.cleaned_data.get('first_name')
      l = self.cleaned_data.get('last_name')
      if Celeb.objects.filter(first_name = f, last_name = l).count() != 0:
          self.errors['first_name'] = 'This celebrity existed'
          return False
      return True
