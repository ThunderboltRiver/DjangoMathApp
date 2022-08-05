from .models import Document
from django.shortcuts import render
from django.views.generic import ListView
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError

# Create your views here.


class Index(ListView):
    model = Document


@requires_csrf_token
def my_customized_server_error(request, template_name="500.html"):
    import sys
    from django.views import debug

    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
