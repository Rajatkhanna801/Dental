from django.urls import path
from .views import Dashboard, ContactView, Services, generate_PDF


urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("services/", Services.as_view(), name="services"),
    path("generate-pdf/", generate_PDF, name="generate-pdf"),
]

