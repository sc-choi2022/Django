from django.shortcuts import render
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        # validation
        if form.is_valid():
            article = form.save()
            return
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)