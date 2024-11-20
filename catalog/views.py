from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...

# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,'num_visits':num_visits},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    """Представление для списка авторов."""
    model = Author
    template_name = 'catalog/author_list.html'  # Убедитесь, что этот шаблон существует
    context_object_name = 'author_list'  # Имя контекста, доступное в шаблоне

class AuthorDetailView(generic.DetailView):
    """Представление для детальной информации об авторе."""
    model = Author
    template_name = 'catalog/author_detail.html'  # Убедитесь, что этот шаблон существуетpy

class LoggedOutView(TemplateView):
    template_name = "registration/logged_out.html"