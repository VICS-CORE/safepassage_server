from django.db import models
from django.utils import timezone
# Create your models here.

class Issuer(models.Model):

    DESIGNATION_CHOICES = [
        ('M', 'Minister'),
        ('C', 'Commissioner'),
        ('P', 'Police Officer'),
    ]
    issuer_name = models.CharField(max_length = 100)
    issuer_designation = models.CharField(max_length=2, choices = DESIGNATION_CHOICES, default='P',)

    def __str__(self):
        return self.issuer_name



class Passes(models.Model):
    PASS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('W', 'Withheld'),
        ('R', 'Rejected'),
    ]
    PASS_TYPE = [
        ('P', 'Permanent'),
        ('O', 'OneTime'),
        ('T', 'Temporary'),
    ]
    PASS_STATE_VALIDITY = [
        ('TN', 'Tamil Nadu'),
        ('KE', 'Kerala'),
        ('AP', 'Andhra Pradesh'),
        ('KA', 'Karnataka'),
        ('TE', 'Telangana'),
        ('NIL', 'Nil'),
    ]
    PASS_MEDICAL_VERIFICATION = [
        ('Y', 'required'),
        ('N', 'notrequired'),
    ]
    pass_type = models.CharField(max_length=2, choices=PASS_TYPE, default='O')
    pass_username = models.CharField(max_length=250, blank=True)
    pass_user_phonenumber = models.IntegerField()
    pass_user_aadhar_number = models.CharField(max_length=12)
    pass_issuer_id = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    pass_issued_time = models.DateTimeField(default=timezone.now)
    pass_start_time = models.DateTimeField(default=timezone.now)
    pass_end_time = models.DateTimeField(default=timezone.now)
    pass_vehicle = models.CharField(max_length=25, blank=True)
    pass_people_count = models.IntegerField()
    pass_state_validity = models.CharField(max_length=3, choices=PASS_STATE_VALIDITY, default='NIL')
    pass_status = models.CharField(max_length=2, choices=PASS_CHOICES, default='P')
    pass_medical_verification = models.CharField(max_length=2, choices=PASS_MEDICAL_VERIFICATION, default='N')
    pass_description = models.CharField(max_length=20000)
    pass_user_pic = models.ImageField(upload_to='', blank=True)
    pass_qr_pic = models.ImageField(upload_to='', blank=True)
    #pass_user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.pass_username
