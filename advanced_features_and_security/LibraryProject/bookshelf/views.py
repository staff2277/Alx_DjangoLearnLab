from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import BookSearchForm, ExampleForm
from .models import Article, Book
from django.db.models import Q

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all() 
    form = BookSearchForm(request.GET or None)
    if form.is_valid():
        search_query = form.cleaned_data.get("search_query")
        if search_query:
            books = books.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))

    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/view.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    return render(request, 'articles/create.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return render(request, 'articles/delete.html')