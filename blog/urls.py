from django.urls import path, include
from .views import *

app_name = 'Blog'
urlpatterns = [
    path('home/<str:username>/blogs/', BlogListView.as_view(), name='blog_list'),
    path('home/<str:username>/create/', CreateBlogView.as_view(), name='create_blog'),
    path('home/detail/<uuid:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('home/update/<uuid:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('home/delete/<uuid:pk>/', delete_memo, name='blog_delete')
]
# 上記のような動的なURLを指定するときは、HTMLでhref={% url "" user.username %},
# また、フォームを送るときはaction={% url "" user.username %}という風に引数を渡さなければならない
