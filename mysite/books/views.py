from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Books, Author, Publisher


#-----TemplateView
class BooksModelView(TemplateView) : 
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Books', 'Author', 'Publisher']
        return context

#-----ListView
class BookList(ListView) :
    model = Books

class AuthorList(ListView) :
    model = Author

class PublisherList(ListView) :
    model = Publisher

#-----DetailView
class BookDetail(DetailView) :
    model = Books

class AuthorDetail(DetailView) :
    model = Author

class PublisherDetail(DetailView) :
    model = Publisher