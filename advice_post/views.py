from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    object_list = Post.objects.all()  # filter(status='Published')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/article/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    post.views += 1
    post.save()
    return render(request, 'post/article/detail.html', {'post': post})


def post_search(request):
    queryset = request.GET.get('q')
    object_list = Post.objects.filter(title__contains=queryset)  # status='Published',
    # context['last_queryset'] = '?q={}'.format('+'.join(queryset.split(' ')))
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/article/search_results.html', {'page': page, 'posts': posts})
