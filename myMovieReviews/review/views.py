from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Review
from django.db.models import F

def review(request):
  sort_by = request.GET.get('sort', 'title')
  valid_sort_options = ['title', 'starrating', 'runningtime']
  if sort_by not in valid_sort_options: # 유효하지 않은 값은 title로 초기화
    sort_by = 'title'
  reviews = Review.objects.order_by(F(sort_by).asc())
  for review in reviews:
    review.display_runningtime = review.formatted_runningtime()
  context = { 'reviews':reviews,
              'current_sort': sort_by,
  }
  return render(request, 'review/review.html', context)

def review_create(request):
  if request.method == 'POST':
    jenre = request.POST['jenre']
    if jenre == 'none':
      return render(request, 'review/create.html', {'error': '장르를 선택해주세요.'})
    review = Review.objects.create(
      title = request.POST['title'],
      year = request.POST['year'],
      jenre = jenre,
      starrating = request.POST['starrating'],
      runningtime = request.POST['runningtime'],
      content = request.POST['content'],
      director = request.POST['director'],
      actor = request.POST['actor'],
    )
    return redirect(reverse('review:review'))
  return render(request, 'review/create.html')

def review_detail(request, pk):
  reviews = Review.objects.get(id=pk)
  context = {
    'review':reviews,
    'display_runningtime':reviews.formatted_runningtime(),
  }
  return render(request, 'review/detail.html', context)

def review_update(request, pk):
  review = Review.objects.get(id=pk)
  if request.method == 'POST':
    jenre = request.POST.get('jenre')
    if jenre == 'none':
      return render(request, 'review/update.html', {'error': '장르를 선택해주세요.'})
    newtitle = request.POST.get('title')
    newyear = request.POST.get('year')
    newjenre = jenre
    newstarrating = request.POST.get('starrating')
    newrunningtime = request.POST.get('runningtime')
    newcontent = request.POST.get('content')
    newdirector = request.POST.get('director')
    newactor = request.POST.get('actor')
    review.title = newtitle
    review.year = newyear
    review.jenre = newjenre
    review.starrating = newstarrating
    review.runningtime = newrunningtime
    review.content = newcontent
    review.director = newdirector
    review.actor = newactor
    review.save()
    return redirect('review:review_detail', pk=review.pk)
  context = {
    'review':review
  }
  return render(request, 'review/update.html', context)

def review_delete(request, pk): # delete는 get 방식으로 받아올 수 없음
  if request.method == 'POST':
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('review:review')
  return redirect('home:index') # get 방식으로 받아올 경우 메인으로 돌아가게 함