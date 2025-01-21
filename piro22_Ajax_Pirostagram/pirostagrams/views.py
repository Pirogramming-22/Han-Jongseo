from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from comments.models import Comment

def pirostagram(request):
  posts = Post.objects.all()
  ctx = {
      'posts': posts,
  }
  return render(request, 'pirostagram.html', ctx)

def post_new(request):
  if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('pirostagrams:pirostagram')
      else:
          ctx = {
              'form': form,
          }
          return render(request, 'post_new.html', ctx)
  elif request.method == 'GET':
      form = PostForm()
      ctx = {
          'form': form,
      }
      return render(request, 'post_new.html', ctx)

def post(request, pk):
  posts = Post.objects.get(id=pk)
  comments = Comment.objects.filter(post=posts)
  ctx = {
      'post': posts,
      'comment': comments,
  }
  return render(request, 'post.html', ctx)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = Post.objects.get(id=post_id)

    post.like += 1
    
    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})