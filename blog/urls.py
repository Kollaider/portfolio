from django.urls import path

from blog.views import LBlogView, blog_detail, blog_category #blog_index, blog_detail,

app_name = 'blog'

urlpatterns = [
    path('', LBlogView.as_view(), name='blog_index'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
    path('<category>/', blog_category, name='blog_category'),
]