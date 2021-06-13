from django.shortcuts import render
from .models import News
from django.views.generic import DetailView

def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details_view.html'
    context_object_name = 'article'

