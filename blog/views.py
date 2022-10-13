from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from blog.models import Post, Category, Comment
from blog.form import CommentForm


# def blog_index(request):
#     posts = Post.objects.all().order_by('created_at')
#     return render(request, 'blog/blog_index.html', {'posts': posts})


class LBlogView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    # queryset = Post.objects.all().order_by('-created_at')
    def get_queryset(self):
        posts = Post.objects.all().order_by('-created_at').filter(pk__in=[1,3])
        return posts


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/blog_detail.html', context=context)







def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('created_at')
    context = {'posts': posts, 'category': category}
    return render(request, 'blog/blog_category.html', context=context)
