from django.urls import path
from .views import AppointementView


urlpatterns = [
    path("appointment/", AppointementView.as_view(), name="new-user")
]