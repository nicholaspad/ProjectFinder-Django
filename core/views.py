from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["netid"] = self.request.user.uniauth_profile.get_display_id()
        return context
