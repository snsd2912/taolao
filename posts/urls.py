from django.urls import path

from . import views

from posts.views import (
  ListPostView,
)

app_name='posts'

urlpatterns = [
    # path('list-posts/$', ListPostView.as_view(), name='list-posts'),
    path('', ListPostView.as_view(), name='list-posts'),
]