import re

from django.contrib.auth.models import User
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
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        netid = self.request.user.uniauth_profile.get_display_id()

        response = HttpResponse()
        if (
            not re.match(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$", email)
            or len(first_name) < 1
            or len(last_name) < 1
            or not netid
        ):
            response.status_code = 400
            return response

        User.objects.filter(username=f"cas-princeton-{netid}").update(
            email=email, first_name=first_name, last_name=last_name
        )

        response.status_code = 201
        return response
