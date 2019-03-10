from django.forms import ModelForm, ValidationError
from .models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        cate = cleaned_data.get('cate_name')
        if Category.objects.filter(cate_name=cate).count() != 0:
            raise ValidationError('This category existed')
