from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse_lazy

# Create your models here.


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
