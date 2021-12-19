from django.urls import path
from .views import Registration, NewPatientForm


urlpatterns = [
    path("new-user/", Registration.as_view(), name="new-user"),
    path("new-patient/", NewPatientForm.as_view(), name="new-form"),
]