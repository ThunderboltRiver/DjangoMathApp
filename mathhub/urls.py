from django.urls import path
from . import views

urlpatterns = [
    path("document/", views.DocumentView.as_view(), name="mathhub-document"),
    path(
        "document/<int:document_id>/",
        views.question_of_document,
        name="document_question",
    ),
    # path("create/", views.Create.as_view(), name="create"),
    # path("update/<pk>", views.Update.as_view(), name="update"),
    # path("delete/<pk>", views.Delete.as_view(), name="delete"),
]
