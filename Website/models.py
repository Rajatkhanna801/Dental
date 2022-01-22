from django.db import models


class DashboardContent(models.Model):
    quote = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return self.quote


class SmileSection(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactDetails(models.Model):
    clinic_name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='pictures', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    fb_link = models.CharField(max_length=200, null=True, blank=True)
    twitter_link = models.CharField(max_length=200, null=True, blank=True)
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.clinic_name


class FAQImage(models.Model):
    faq_image = models.ImageField(upload_to='pictures', null=True, blank=True)


class FAQ(models.Model):
    question = models.CharField(max_length=1000, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    sort_by = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['sort_by']

    def __str__(self):
        return self.question


class Stats(models.Model):
    Performed_surgeries = models.PositiveBigIntegerField(null=True, blank=True)
    Satisfied_patients = models.PositiveBigIntegerField(null=True, blank=True)
    StaffMembers = models.PositiveBigIntegerField(null=True, blank=True)
    Yearly_surgeries = models.PositiveBigIntegerField(null=True, blank=True)


class Description(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return self.title


class WhatWeOffer(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE, null=True, blank=True)
    our_services = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.our_services


class FotterContent(models.Model):
    quote = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return self.content


class QuestionSection(models.Model):
    quote = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return self.content


class QuestionIcon(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    
    def __str__(self):
        return self.content


class FotterIcon(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class ServiceDashboard(models.Model):
    quote = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    

class OurServices(models.Model):
    service_name = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)




