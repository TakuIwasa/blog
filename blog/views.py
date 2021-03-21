from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from .models import Article


class ArticleListView(generic.ListView):
    model = Article

    def get_queryset(self):
        queryset = Article.objects.order_by('-date')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset