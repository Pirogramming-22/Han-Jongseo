from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    return render(request, 'ideas/ideas_create.html', context=ctx)
  else:
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
      new_idea = form.save()
      return redirect(reverse('ideas:ideas_detail', kwargs={'pk': new_idea.id}))
    else:
      ctx = {'form': form}
      return render(request, 'ideas/ideas_create.html', context=ctx)

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
    return redirect(reverse('ideas:ideas_detail', kwargs={'pk': pk}))

@csrf_exempt
def toggle_IdeaStar(request, idea_id):
  if request.method == "POST":
    idea = get_object_or_404(Idea, id=idea_id)
    idea.is_IdeaStar = not idea.is_IdeaStar
    idea.save()
    return JsonResponse({"is_IdeaStar": idea.is_IdeaStar})
  return JsonResponse({"error": "Invalid request"}, status=400)