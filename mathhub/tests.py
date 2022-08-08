from django.test import TestCase, RequestFactory, Client
from django.urls import resolve
from django.db import models
from .views import DocumentView, question_of_document
from .models import Document

# Create your tests here.
class DocumentViewTest(TestCase):
    def setUp(self) -> None:
        self.document = Document.objects.create(
            title="test_document", author="test_author"
        )

    def test_documentview_shoud_iclude_created_document(self):
        saved_documents = Document.objects.all()
        self.assertIn(self.document, saved_documents)

    def test_get_queryset_shoud_return_list_including_created_document(self):
        request = RequestFactory().get("/mathhub/document/?title=test_document")
        view = DocumentView()
        view.setup(request)
        queryset = view.get_queryset()
        self.assertIn(self.document, queryset)

    def test_document_view_return_200_and_expected_title(self):
        response = self.client.get("/mathhub/document/")
        self.assertContains(response, "Mathhub", status_code=200)

    def test_document_view_uses_expected_template(self):
        response = self.client.get("/mathhub/document/")
        self.assertTemplateUsed(response, "mathhub/document_list.html")


class DocumentDetailTest(TestCase):
    def test_question_of_document_return_(self):
        found = resolve("/mathhub/document/1/")
        self.assertEqual(question_of_document, found.func)
