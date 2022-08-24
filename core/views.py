import re

from django.http import HttpResponse
from django.views import generic

from .models import Config


class IndexView(generic.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = Config.objects.first()
        context["netid"] = self.request.user.uniauth_profile.get_display_id()
        context["config"] = config
        return context

    def post(self, request):
        email = request.POST.get("email")
        name = request.POST.get("name")

        response = HttpResponse()
        if (
            not re.match(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$", email)
            or len(name) < 1
        ):
            response.status_code = 400
            return response

        print("success", email, name)

        response.status_code = 201
        return response
