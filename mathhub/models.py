from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# Create your models here.
UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
    )


class Document(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    created = models.DateTimeField(
        auto_now_add=True, editable=False, blank=False, null=False
    )

    updated = models.DateField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
    )
    author = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    publisher = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    totalpage = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=1,
    )


class Question(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    document_id = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, null=False, blank=False, default="title")
    body = models.TextField(null=False, blank=False, default="body")
    page_num = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=1,
    )
    column_num = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=1,
    )
