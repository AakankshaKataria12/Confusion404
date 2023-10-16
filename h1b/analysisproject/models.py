from django.db import models

# Create your models here.

class Application(models.Model):
    case_number = models.CharField(max_length=255, unique=True)
    case_status = models.CharField(max_length=255)
    case_submitted = models.DateTimeField()
    decision_date = models.DateTimeField()
    visa_class = models.CharField(max_length=255)

class Employment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    employment_start_date = models.DateField()
    employment_end_date = models.DateField()
    employer_name = models.CharField(max_length=255)
    employer_address1 = models.CharField(max_length=255)
    employer_address2 = models.CharField(max_length=255, blank=True, null=True)
    employer_city = models.CharField(max_length=255)
    employer_state = models.CharField(max_length=255)
    employer_postal_code = models.CharField(max_length=20)
    employer_country = models.CharField(max_length=255)
    employer_province = models.CharField(max_length=255, blank=True, null=True)
    employer_phone = models.CharField(max_length=20)
    employer_phone_ext = models.CharField(max_length=10, blank=True, null=True)

class AgentAttorney(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    agent_attorney_name = models.CharField(max_length=255)
    agent_attorney_city = models.CharField(max_length=255)
    agent_attorney_state = models.CharField(max_length=255)

class Job(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    soc_code = models.CharField(max_length=20)
    soc_name = models.CharField(max_length=255)
    naic_code = models.CharField(max_length=20)

class LaborCondition(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    total_workers = models.PositiveIntegerField()
    full_time_position = models.BooleanField()
    prevailing_wage = models.DecimalField(max_digits=10, decimal_places=2)
    pw_unit_of_pay = models.CharField(max_length=20)
    pw_wage_source = models.CharField(max_length=20)
    pw_wage_source_year = models.PositiveSmallIntegerField()
    pw_wage_source_other = models.TextField(blank=True, null=True)
    wage_rate_of_pay_from = models.DecimalField(max_digits=10, decimal_places=2)
    wage_rate_of_pay_to = models.DecimalField(max_digits=10, decimal_places=2)
    wage_unit_of_pay = models.CharField(max_length=20)
    h1b_dependent = models.BooleanField()
    willful_violator = models.BooleanField()

class Worksite(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    worksite_city = models.CharField(max_length=255)
    worksite_county = models.CharField(max_length=255)
    worksite_state = models.CharField(max_length=255)
    worksite_postal_code = models.CharField(max_length=20)

class OriginalCertification(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    original_cert_date = models.DateField()