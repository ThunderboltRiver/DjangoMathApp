from .models import Document
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import DocumentForm
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse, HttpResponseServerError
from django.db.models import Q

# Create your views here.


class DocumentView(FormView, ListView):
    form_class = DocumentForm
    context_object_name = "document_list"
    model = Document

    def get_queryset(self):
        queryset = Document.objects.order_by("-created")
        query = self.request.GET.get("title")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(auther__icontains=query)
            )
        return queryset

    def __str__(self) -> str:
        return "Mathhub Documents"


def question_of_document(request, document_id):
    return HttpResponse("ドキュメントの質問一覧")


@requires_csrf_token
def my_customized_server_error(request, template_name="500.html"):
    import sys
    from django.views import debug

    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
