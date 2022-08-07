from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "資料名で検索"}
            ),
        }
