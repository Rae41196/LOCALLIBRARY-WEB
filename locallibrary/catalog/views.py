from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""
    #generate counts of some of the main objects
    num_books = Book.objects.all().count()#objects.all will fetch the  records
    num_instances = BookInstance.objects.all().count()


    #Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    #The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_author': num_authors,
    }
    #rendeer the HTML template index.html with data in context variable
    return render(request, 'index.html', context = context)

    # class BookListView(generic.ListView):
    #     model = Book
    #     context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #     queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    #     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

class BookDetailView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.ListView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context