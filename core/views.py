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
