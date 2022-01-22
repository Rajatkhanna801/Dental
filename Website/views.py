from django.shortcuts import render, redirect
from django.views import View
from .models import FAQ, ContactDetails, Stats, Description, \
    DashboardContent, FAQImage, SmileSection, FotterContent,\
    QuestionSection, QuestionIcon, FotterIcon, OurServices, ServiceDashboard
from Dental.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa 


def generate_PDF(request):
    data = {}
    template = get_template('form.html')
    html  = template.render(data)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()            
    return HttpResponse(pdf, 'application/pdf')


class Dashboard(View):
    def get(self, request):
        context = {
            "FAQ":FAQ.objects.all(),
            "contact_details":ContactDetails.objects.all().last(),
            "stats":Stats.objects.all().last(),
            "Description":Description.objects.all(),
            "faq_image" : FAQImage.objects.all().last(),
            "smile_section" : SmileSection.objects.all().last(),
            "fotter_content" : FotterContent.objects.all().last(),
            "ques_section" : QuestionSection.objects.all().last(),
            "ques_icon" : QuestionIcon.objects.all(),
            "fotter_icon" : FotterIcon.objects.all(),
            "content" : DashboardContent.objects.all().last()

        }
        return render(request, "index.html", context)


class ContactView(View):
    def get(self, request):
        context = dict()
        context['contact_details'] = ContactDetails.objects.all().last()
        return render(request, "contact.html", context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        text_message = request.POST.get('message')
        subject = "Customer Query"
        print("====", first_name, last_name, email, phone_number, text_message)
        new_line = "/n"
        message = f"Name: {first_name} {last_name}, Email: {email}, Phone_number: {phone_number}, Message: {text_message}"
        send_mail(subject,message, EMAIL_HOST_USER, ['sakshikhanna133@gmail.com'], fail_silently = False)
        return redirect('contact')


class Services(View):
    def get(self, request, *args, **kwargs):
        content = dict()
        content['abc'] = ServiceDashboard.objects.last()
        content['all_services'] = OurServices.objects.all()
        content['contact_details'] = ContactDetails.objects.all().last()
        return render(request, "services.html", content)