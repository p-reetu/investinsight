from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import smtplib


@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    try:
        if created and instance.email:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            message = f"Subject: Welcome!\n\nWelcome to Invest Insight, {instance.username}!"
            s.sendmail(settings.EMAIL_HOST_USER, instance.email, message)
            s.quit()
            print("Email sent")
    except Exception as e:
        print("Email sending failed:", e)