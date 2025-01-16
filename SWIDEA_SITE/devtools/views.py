from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Devtool
from .forms import DevtoolForm

def devtools(request):
  devtools = Devtool.objects.all()
  paginator = Paginator(devtools, 8)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  ctx = {
    'page_obj': page_obj,
  }
  return render(request, 'devtools/devtools.html', context=ctx)

def devtools_create(request):
  if request.method == 'POST':
    devtool = Devtool.objects.create(
      name = request.POST['name'],
      kind = request.POST['kind'],
      content = request.POST['content'],
    )
    return redirect(reverse('devtools:devtools_detail', kwargs={'pk': devtool.id}))
  return render(request, 'devtools/devtools_create.html')

def devtools_detail(request, pk):
  devtools = Devtool.objects.get(id=pk)
  related_ideas = devtools.idea_set.all()
  context = {
    'devtool': devtools,
    'related_ideas': related_ideas,
  }
  return render(request, 'devtools/devtools_detail.html', context)

def devtools_update(request, pk):
  devtool = Devtool.objects.get(id=pk)
  if request.method == 'POST':
    devtool.name = request.POST.get('name')
    devtool.kind = request.POST.get('kind')
    devtool.content = request.POST.get('content')
    devtool.save()
    return redirect('devtools:devtools_detail', pk=devtool.pk)
  form = DevtoolForm(instance=devtool)
  ctx = {
    'form': form,
    'pk': pk
  }
  return render(request, 'devtools/devtools_update.html', context=ctx)

def devtools_delete(request, pk):
  Devtool.objects.get(id=pk).delete()
  return redirect('devtools:devtools')