from django.urls import path
from .views import Dashboard, ContactView, Services


urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("services/", Services.as_view(), name="services"),
]

