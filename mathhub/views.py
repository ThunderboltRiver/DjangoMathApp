from xml.dom.minidom import Document
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class Index(ListView):
    model = Document
