from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from .models import Category


def add_cate(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            cate.save()
            return redirect('cate')
    else:
        form = CategoryForm()
    return render(request, 'category/cate_form.html', {'form': form})

def edit_cate(request, cate_id=None):
    item = get_object_or_404(Category, id=cate_id)
    form = CategoryForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('cate')
    return render(request, 'category/cate_form.html', {'form': form})

def cate(request):
    return render(request, 'category/cate.html', {'cate_list': Category.objects.all()})

def delete_cate(request, cate_id=None):
    Category.objects.get(id=cate_id).delete()
    return redirect('cate')
