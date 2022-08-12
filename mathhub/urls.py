from django.urls import path
from . import views

urlpatterns = [
    path("document/", views.DocumentView.as_view(), name="mathhub-document"),
    path(
        "document/<int:pk>/",
        views.DocumentDetail.as_view(),
        name="document-detail",
    ),
    # path("create/", views.Create.as_view(), name="create"),
    # path("update/<pk>", views.Update.as_view(), name="update"),
    # path("delete/<pk>", views.Delete.as_view(), name="delete"),
]
