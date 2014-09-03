from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

import string, random, logging

from twilio.rest import TwilioRestClient

from sms_verification import twilio_secrets

from verifier.models import VerificationCode, VERIFICATION_CODE_LENGTH

logger = logging.getLogger(__name__)
twilio = TwilioRestClient(twilio_secrets.TWILIO_ACCOUNT_SID, twilio_secrets.TWILIO_AUTH_TOKEN)

def send_code(request):
    try:
        phone_number = request.GET['phone_number']
    except KeyError:
        return HttpResponse("No phone number provided.", status = 400)
    code = ''.join([random.choice(string.digits) for _ in range(VERIFICATION_CODE_LENGTH)])
    VerificationCode.objects.filter(phone_number = phone_number).delete()
    verification_code = VerificationCode(phone_number = phone_number, code = code)
    try:
        twilio_message = twilio.messages.create(
            body = ("Your SMS Verification Test verification code is: %s" % code),
            to = phone_number,
            from_ = "+17315990087"
        )
    except twilio.TwilioRestException as error:
        return HttpResponse("Error sending verification SMS: %s" % str(error), status = 400)
    verification_code.save()
    return HttpResponse()
    

def check_code(request):
    try:
        verification_code = get_list_or_404(VerificationCode, phone_number = request.GET['phone_number'])[0]
    except KeyError:
        return HttpResponse("No phone number provided.", status = 400)
    try:
        code = request.GET["code"]
    except KeyError:
        return HttpResponse("No code provided.", status = 400)
    result = None
    if(code == verification_code.code):
        result = HttpResponse("Success! You've verified.")
    else:
        result = HttpResponse("Invalid or incorrect code.")
    verification_code.delete()
    return result
    