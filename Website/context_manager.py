from .models import ContactDetails


def ContactDetails(request):
    return {'contact_details' : ContactDetails.objects.all().last()}