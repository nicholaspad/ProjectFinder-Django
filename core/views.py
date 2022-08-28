import re

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import generic

from .models import Config, Entry
from .utils import get_username_from_netid, is_past_due


class IndexView(generic.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        netid = self.request.user.uniauth_profile.get_display_id()
        config = Config.objects.first()
        entries = Entry.objects.all().order_by("author__last_name")
        user = User.objects.filter(username=get_username_from_netid(netid)).first()
        context["netid"] = netid
        context["config"] = config
        context["user"] = user
        context["has_completed_settings"] = (
            user
            and len(user.email) > 0
            and len(user.first_name) > 0
            and len(user.last_name) > 0
        )
        context["has_created_entry"] = hasattr(user, "entry")
        context["is_past_due"] = is_past_due()
        context["user_entry"] = user.entry if hasattr(user, "entry") else {}

        context["table_data"] = [
            {
                "name": f"{entry.author.first_name} {entry.author.last_name}",
                "netid": entry.author.username.split("-")[-1],
                "skills": entry.skills.split(", "),
                "interests": entry.interests,
                "project_name": entry.project_name,
                "project_description": entry.project_description,
            }
            for entry in entries
        ]

        return context


class UpdateSettingsView(generic.View):
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

        User.objects.filter(username=get_username_from_netid(netid)).update(
            email=email.strip(),
            first_name=first_name.strip(),
            last_name=last_name.strip(),
        )

        response.status_code = 201
        return response


class CreateOrUpdateEntryView(generic.View):
    def post(self, request):
        skills = request.POST.get("skills")
        interests = request.POST.get("interests")
        project_name = request.POST.get("projectName")
        project_description = request.POST.get("projectDescription")
        netid = self.request.user.uniauth_profile.get_display_id()
        config = Config.objects.first()

        response = HttpResponse()
        if len(skills) < 1 or len(interests) < 1 or not netid or is_past_due():
            response.status_code = 400
            return response

        Entry.objects.update_or_create(
            author__username=get_username_from_netid(netid),
            defaults={
                "author": User.objects.filter(
                    username=get_username_from_netid(netid)
                ).first(),
                "skills": ", ".join(
                    filter(None, [e.strip() for e in skills.split(",")])
                ),
                "interests": interests.strip(),
                "project_name": project_name.strip(),
                "project_description": project_description.strip(),
            },
        )

        response.status_code = 201
        return response


class DeleteEntryView(generic.View):
    def post(self, request):
        netid = self.request.user.uniauth_profile.get_display_id()

        response = HttpResponse()
        if not netid:
            response.status_code = 400
            return response

        Entry.objects.filter(author__username=get_username_from_netid(netid)).delete()

        response.status_code = 201
        return response
