from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Idea
from .forms import IdeaForm

def main(request):
  ideas = Idea.objects.all()
  paginator = Paginator(ideas, 4)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  ctx = {
    
    'page_obj': page_obj,
  }
  return render(request, 'ideas/main.html', context=ctx)

def ideas_create(request):
  if request.method == 'GET':
    form = IdeaForm()
    ctx = {'form': form}
    return render(request, 'ideas/ideas_create.html', context = ctx)
  else:
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    return redirect('/')

def ideas_detail(request, pk):
  target_idea = Idea.objects.get(id=pk)
  ctx = {'idea': target_idea,
          }
  return render(request, 'ideas/ideas_detail.html', context=ctx)

def ideas_delete(request, pk):
  Idea.objects.get(id=pk).delete()
  return redirect('ideas:main')

def ideas_update(request, pk):
  if request.method == 'GET':
    idea = Idea.objects.get(id=pk)
    form = IdeaForm(instance=idea)
    ctx = {'form': form,
            'pk': pk}
    return render(request, 'ideas/ideas_update.html', context=ctx)
  else:
    idea = Idea.objects.get(id=pk)
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
      form.save()
    return redirect(f'/ideas/ideas_detail/{pk}', pk)
