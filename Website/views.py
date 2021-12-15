from django.shortcuts import render, redirect
from django.views import View
from .models import FAQ, ContactDetails, Stats, Description, \
    DashboardContent, FAQImage, SmileSection, FotterContent,\
    QuestionSection, QuestionIcon, FotterIcon, OurServices, ServiceDashboard
from Dental.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


class Dashboard(View):
    def get(self, request):
        context = dict()
        context['FAQ'] = FAQ.objects.all()
        context['contact_details'] = ContactDetails.objects.all().last()
        context['stats'] = Stats.objects.all().last()
        context['Description'] = Description.objects.all()
        context['content'] = DashboardContent.objects.all().last()
        context['faq_image'] = FAQImage.objects.all().last()
        context['smile_section'] = SmileSection.objects.all().last()
        context['fotter_content'] = FotterContent.objects.all().last()
        context['ques_section'] = QuestionSection.objects.all().last()
        context['ques_icon'] = QuestionIcon.objects.all()
        context['fotter_icon'] = FotterIcon.objects.all()
        return render(request, "index.html", context)


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        print("====", first_name, last_name, email, phone_number, message)
        subject = [first_name, last_name, email, phone_number, message]
        send_mail(subject,message, EMAIL_HOST_USER, ['rajatkhanna802@gmail.com'], fail_silently = False)
        return redirect('contact')


class Services(View):
    def get(self, request, *args, **kwargs):
        content = dict()
        content['abc'] = ServiceDashboard.objects.last()
        content['all_services'] = OurServices.objects.all()
        content['contact_details'] = ContactDetails.objects.all().last()
        return render(request, "services.html", content)