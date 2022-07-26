from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from . models import TodoModel


class TodoCreateView(CreateView):
    model = TodoModel
    fields = [
        'title',
        'description',
        'time'
    ]

    template_name = 'home.html'
    success_url = "list.html"

class TodoListView(ListView):
    model = TodoModel
    template_name = "list.html"