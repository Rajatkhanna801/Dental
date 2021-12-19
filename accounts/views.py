from django.shortcuts import render
from django.views import View


class Registration(View):
    template_name = "form.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        return redirect('new-user')


class NewPatientForm(View):
    template_name = "new_form.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
