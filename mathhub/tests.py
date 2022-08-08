from urllib import request
from webbrowser import get
from django.db.models import Q
from django.test import TestCase, RequestFactory, Client
from django.urls import resolve
from .views import DocumentView, question_of_document
from .models import Document

# Create your tests here.
class DocumentViewTest(TestCase):
    def test_document_view_return_200_and_expected_title(self):
        response = self.client.get("/mathhub/document/")
        self.assertContains(response, "Mathhub", status_code=200)

    def test_document_view_uses_expected_template(self):
        response = self.client.get("/mathhub/document/")
        self.assertTemplateUsed(response, "mathhub/document_list.html")


class DocumentQuestionTest(TestCase):
    def test_question_of_document_return_(self):
        found = resolve("/mathhub/document/1/")
        self.assertEqual(question_of_document, found.func)
