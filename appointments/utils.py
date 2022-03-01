from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.conf import settings


def html_to_pdf(data):

    print("data=============", data)
    template_path = "email_send.html"
    response = HttpResponse(content_type='application/pdf')

    html = render_to_string(template_path,data)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=certificate_{}'.format('appointment') + '.pdf'

    pdf = weasyprint.HTML(string=html).write_pdf()

    to_emails = ['rajatkhanna801@gmail.com']
    subject = "New Appointment"
    email = EmailMessage(subject, body=pdf, from_email=settings.EMAIL_HOST_USER, to=to_emails)
    email.attach("certificate_{}".format('appointment') + '.pdf', pdf, "application/pdf")
    email.content_subtype = "pdf" 
    email.encoding = 'us-ascii'
    email.send()

    return HttpResponse(pdf, content_type='application/pdf')


MartialStatusChoices = (
    ("Single", "Single"),
    ("Married", "Married"),
    ("Child", "Child"),
    ("other", "other"),
)
GenderChoice = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("other", "other"),
)

