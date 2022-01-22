from django.contrib import admin
from .models import FAQ, ContactDetails, Stats, WhatWeOffer, \
    DashboardContent, Description, FAQImage, SmileSection, \
    FotterContent, QuestionSection, \
    QuestionIcon, FotterIcon, OurServices, ServiceDashboard


@admin.register(ContactDetails)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['clinic_name', 'email', 'phone_number', 'address', 'opening_time', 'closing_time']


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['Performed_surgeries', 'Satisfied_patients', 'StaffMembers', 'Yearly_surgeries']
    list_editable = ['Satisfied_patients', 'StaffMembers', 'Yearly_surgeries']


@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'image']


@admin.register(ServiceDashboard)
class ServiceDashboardAdmin(admin.ModelAdmin):
    list_display = ['quote','content', 'image']


admin.site.register(FAQ)
admin.site.register(WhatWeOffer)
admin.site.register(DashboardContent)
admin.site.register(Description)
admin.site.register(FAQImage)
admin.site.register(SmileSection)
admin.site.register(FotterContent)
admin.site.register(QuestionSection)
admin.site.register(QuestionIcon)
admin.site.register(FotterIcon)