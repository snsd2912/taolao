from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Post

class ListPostView(ListView):
  model = Post
  def get (self, request, *args, **kwargs):
    template_name = 'posts/list-posts.html' # sẽ được tạo ở phần dưới
    obj = {
      'posts': Post.objects.all()
    }
    return render(request, template_name, obj)