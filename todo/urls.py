from django.urls import path
from .views import TodoCreateView, TodoListView

urlpatterns = [
    path('',TodoCreateView.as_view(), name="home"),
    path('list/', TodoListView.as_view())
]
