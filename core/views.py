import re

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import generic

from .models import Config, Entry


class IndexView(generic.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        netid = self.request.user.uniauth_profile.get_display_id()
        config = Config.objects.first()
        entries = Entry.objects.all().order_by("author__last_name")
        user = User.objects.filter(username=f"cas-princeton-{netid}").first()
        context["netid"] = netid
        context["config"] = config
        context["user"] = user
        context["has_created_entry"] = hasattr(user, "entry")

        context["table_data"] = [
            {
                "name": f"{entry.author.first_name} {entry.author.last_name}",
                "netid": entry.author.username.split("-")[-1],
                "skills": [e.strip() for e in entry.skills.split(",")],
                "interests": entry.interests,
                "project_name": entry.project_name,
                "project_description": entry.project_description,
            }
            for entry in entries
        ]

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
