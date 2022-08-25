from django.urls import path
from uniauth.decorators import login_required

from ProjectFinder.settings import LOGIN_URL

from . import views

app_name = "core"
urlpatterns = [
    path(
        "", login_required(views.IndexView.as_view(), login_url=LOGIN_URL), name="index"
    ),
    path(
        "update-settings",
        login_required(views.UpdateSettingsView.as_view(), login_url=LOGIN_URL),
        name="update-settings",
    ),
    path(
        "create-or-update-entry",
        login_required(views.CreateOrUpdateEntryView.as_view(), login_url=LOGIN_URL),
        name="create-or-update-entry",
    ),
]
