from django.shortcuts import render, redirect
from django.views import View
from Website.models import ContactDetails
from appointments.models import Appointments
import weasyprint


class AppointementView(View):
    template_name = "form.html"
    def get(self, request):
        context = {}
        context['contact_details'] = ContactDetails.objects.all().last()
        return render(request, self.template_name, context)

    def post(self, request):
        field_name_list = [i.name for i in Appointments._meta.fields if i.name !="id"]
        appointment_list = {keys:request.POST.get(keys) for keys in field_name_list}
        for key, value in dict(appointment_list).items():
            if value is None:
                del appointment_list[key]
        # print("appointment_list================", appointment_list)
        Appointments.objects.create(**appointment_list)

        return redirect('dashboard')

