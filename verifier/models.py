from django.db import models

VERIFICATION_CODE_LENGTH = 5

class VerificationCode(models.Model):
    phone_number = models.CharField(max_length=20)
    code = models.CharField(max_length=VERIFICATION_CODE_LENGTH)
