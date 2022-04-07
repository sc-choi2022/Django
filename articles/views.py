from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        # validation
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)