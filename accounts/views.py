from django.shortcuts import render
from django.views import View


class Registration(View):
    template_name = "patient_form.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        return redirect('new-user')
