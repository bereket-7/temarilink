from apps.notifications.models import SMSMessage

def send_sms(school, phone, message):
    """
    Mock SMS service to send messages to parents/guardians.
    In a real scenario, this would call an external API provider.
    """
    # Simply log the attempt by creating a record in our database
    try:
        SMSMessage.objects.create(
            school=school,
            phone=phone,
            message=message,
            status=SMSMessage.SENT
        )
        print(f"SMS SENT to {phone}: {message}")
        return True
    except Exception as e:
        print(f"SMS FAILED to {phone}: {e}")
        return False
