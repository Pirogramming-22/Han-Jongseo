from django.shortcuts import redirect
from .models import Post
from .models import Comment

def comment_create(request, pk):
  if request.method == 'POST':
    findPost = Post.objects.get(id=pk)
    Comment.objects.create(
      post = findPost,
      content = request.POST['content']
    )
    return redirect('pirostagrams:post', pk=findPost.id)
  
def comment_delete(request, pk):
  if request.method == 'POST':
    findComment = Comment.objects.get(id=pk)
    post_pk = findComment.post.id
    findComment.delete()
    return redirect('pirostagrams:post', pk=post_pk)