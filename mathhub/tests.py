from django.test import TestCase, RequestFactory, Client
from django.urls import resolve
from django.db import models
from django.contrib.auth import get_user_model
from .views import DocumentView
from .models import Document, Question

UserModel = get_user_model()

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
    def setUp(self) -> None:
        self.user = UserModel.objects.create(
            username="test_user_name",
            first_name="test_first_name",
            last_name="test_last_name",
            email="example@test.com",
            password="this_test_password001",
        )

        self.document = Document.objects.create(
            title="test_document",
            author="test_author",
        )

        self.question = Question.objects.create(
            user=self.user,
            document=self.document,
            title="test_question_title",
            body="test_question_body",
            page_num=10,
            column_num=11,
        )

    def test_question_of_document_return_(self):
        client = Client()
        response = client.get("/mathhub/document/1/")
        self.assertTemplateUsed(response, "mathhub/document_detail.html")
