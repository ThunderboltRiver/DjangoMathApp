# Create your views here.
from typing import Any, Dict
from django.views.generic import TemplateView
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name: str = "index.html"

    def get_context_data(self) -> Dict[str, Any]:
        ctxt = super().get_context_data()
        ctxt["username"] = ""
        return ctxt


class AboutView(TemplateView):
    template_name: str = "about.html"

    def get_context_data(self) -> Dict[str, Any]:
        ctxt = super().get_context_data()
        ctxt["num_services"] = 1247
        ctxt["skills"] = ["Python", "JavaScript", "Julia"]
        # ctxt["skills"] = []
        return ctxt
