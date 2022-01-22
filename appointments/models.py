from django_countries.fields import CountryField
from django.db import models
from appointments.utils import MartialStatusChoices, GenderChoice



class Appointments(models.Model):
    appointment_date = models.DateField(
    )
    patient_name = models.CharField(
        max_length=2000
    )
    preferred_name = models.CharField(
        max_length=2000,
        null = True,
        blank = True
    )
    martial_status = models.CharField(
        max_length=2000,
        choices = MartialStatusChoices
    )
    gender = models.CharField(
        max_length=2000,
        choices = GenderChoice
    )
    patient_address = models.TextField(
        null=True, blank=True
    )
    city = models.TextField(
        null=True, blank=True
    )
    state = models.TextField(
        null=True, blank=True
    )
    zip = models.PositiveIntegerField(
        null=True, blank=True
    )
    counrty = CountryField()
    home_number = models.PositiveIntegerField(
        null=True, blank=True
    )
    work_number = models.PositiveIntegerField(
        null=True, blank=True
    )
    cell_number = models.PositiveIntegerField(
        null=True, blank=True
    )
    reminder_via_message = models.BooleanField(
        default=False
    )
    reminder_via_email = models.BooleanField(
        default=False
    )
    email_address = models.EmailField(
        null=True, blank=True
    )
    patient_employer = models.CharField(
        max_length=200
    )
    patient_ocupation = models.CharField(
        max_length=200
    )
    referal_name = models.CharField(
        max_length=200
    )
    patient_relative_name = models.CharField(
        max_length=200
    )
    patient_relative_number = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    relative_relationship = models.CharField(
        max_length=2000,
        null=True,
        blank=True
    )
    relative_phone_number = models.PositiveBigIntegerField(
        null=True, 
        blank=True
    )
    guardian_name = models.CharField(
        max_length=2000,
        null=True,
        blank=True
    )
    guardian_dob = models.DateField(
        null=True, 
        blank=True
    )
    aids = models.BooleanField(
        default=False
    )
    artifical_joints = models.BooleanField(
        default=False
    )
    bloody_sputum = models.BooleanField(
        default=False
    )
    bisphosphonate_medication = models.BooleanField(
        default=False
    )
    cronic_cough = models.BooleanField(
        default=False
    )
    epilepsy = models.BooleanField(
        default=False
    )
    fainting = models.BooleanField(
        default=False
    )
    growths = models.BooleanField(
        default=False
    )
    high_blood_pressure = models.BooleanField(
        default=False
    )
    heart_murmur = models.BooleanField(
        default=False
    )
    hyper_thyroid = models.BooleanField(
        default=False
    )
    Jaundice = models.BooleanField(
        default=False
    )
    loss_appetite = models.BooleanField(
        default=False
    )
    mitral_valve_prolapse = models.BooleanField(
        default=False
    )
    nervous_disorders = models.BooleanField(
        default=False
    )
    prosthetic_heart_valve = models.BooleanField(
        default=False
    )
    respiratory_problems = models.BooleanField(
        default=False
    )
    stomach_problems_ulcers = models.BooleanField(
        default=False
    )
    Sexually_Transmitted_Diseases = models.BooleanField(
        default=False
    )
    Unexplained_Weight_loss = models.BooleanField(
        default=False
    )
    Anemia = models.BooleanField(
        default=False
    )
    Asthma =models.BooleanField(
        default=False
    ) 
    Brast_implants = models.BooleanField(
        default=False
    )
    Cancer = models.BooleanField(
        default=False
    )
    Diabetes = models.BooleanField(
        default=False
    )
    Emphysema = models.BooleanField(
        default=False
    )
    Fatigue = models.BooleanField(
        default=False
    )
    Hay_Fever = models.BooleanField(
        default=False
    )
    Hemoptysis = models.BooleanField(
        default=False
    )
    Hepatitis = models.BooleanField(
        default=False
    )
    Hypo_Thyroid = models.BooleanField(
        default=False
    )
    Kidney_Disease = models.BooleanField(
        default=False
    )
    Mental_Disorders = models.BooleanField(
        default=False
    )
    Night_Sweats = models.BooleanField(
        default=False
    )
    Pacemaker = models.BooleanField(
        default=False
    )
    Rheumatic_Fever = models.BooleanField(
        default=False
    )
    Fadiation_Treatment = models.BooleanField(
        default=False
    )
    Sinus_Probmes = models.BooleanField(
        default=False
    )
    Tuberculosis = models.BooleanField(
        default=False
    )
    Arthritis = models.BooleanField(
        default=False
    )
    Blood_Disease = models.BooleanField(
        default=False
    )
    Blood_Thinners = models.BooleanField(
        default=False
    )
    Chest_Pain = models.BooleanField(
        default=False
    )
    Dizziness = models.BooleanField(
        default=False
    )
    Excessive_Bleeding = models.BooleanField(
        default=False
    )
    Glaucoma = models.BooleanField(
        default=False
    )
    Head_Injury = models.BooleanField(
        default=False
    )
    Heart_Disease = models.BooleanField(
        default=False
    )
    Horaseness = models.BooleanField(
        default=False
    )
    High_Cholesterol = models.BooleanField(
        default=False
    )
    Liver_Disease = models.BooleanField(
        default=False
    )
    Recent_Surgery = models.BooleanField(
        default=False
    )
    Stroke = models.BooleanField(
        default=False
    )
    Transplant = models.BooleanField(
        default=False
    )
    Tumors = models.BooleanField(
        default=False
    )
    Other = models.BooleanField(
        default=False
    )
 



