# Create your views here.
from typing import Any, Dict
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError


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


@requires_csrf_token
def my_customized_server_error(request, template_name="500.html"):
    import sys
    from django.views import debug

    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
