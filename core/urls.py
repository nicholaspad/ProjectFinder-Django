from django.urls import path
from uniauth.decorators import login_required

from ProjectFinder.settings import LOGIN_URL

from . import views

app_name = "core"
urlpatterns = [
    path(
        "", login_required(views.IndexView.as_view(), login_url=LOGIN_URL), name="index"
    )
]
