from django.urls import path
from uniauth.decorators import login_required

from . import views

app_name = "core"
urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="index"),
    path(
        "update-settings",
        login_required(views.UpdateSettingsView.as_view()),
        name="update-settings",
    ),
    path(
        "create-or-update-entry",
        login_required(views.CreateOrUpdateEntryView.as_view()),
        name="create-or-update-entry",
    ),
    path(
        "delete-entry",
        login_required(views.DeleteEntryView.as_view()),
        name="delete-entry",
    ),
]
