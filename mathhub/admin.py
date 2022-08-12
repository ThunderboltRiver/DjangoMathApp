from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
