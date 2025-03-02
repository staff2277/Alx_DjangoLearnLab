from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article

# Create your views here.
@permission_required('your_app_name.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/view.html', {'articles': articles})

@permission_required('your_app_name.can_create', raise_exception=True)
def create_article(request):
    # Logic for creating an article (e.g., form handling)
    return render(request, 'articles/create.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # Logic for editing an article
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return render(request, 'articles/delete.html')