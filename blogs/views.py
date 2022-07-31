from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class Index(ListView):
    model = Post


class Detail(DetailView):
    model = Post


class Create(CreateView):
    model = Post
    fields = ["title", "body", "category", "tags"]


class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]


class Delete(DeleteView):
    model = Post
    success_url = "/"
