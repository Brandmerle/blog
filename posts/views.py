from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model=Post
    template_name = "posts/list.html"

class PostDetailView(DetailView):
    model=Post
    template_name = "posts/new.html"

class PostCreateView(CreateView):
    model=Post
    template_name = "posts/new.html"

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "status"
    ]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")     #Update this if your ListVeiw isnt mapped to "list"