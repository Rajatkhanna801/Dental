from django.urls import path
from .views import Registration


urlpatterns = [
    path("new-user/", Registration.as_view(), name="new-user"),
]