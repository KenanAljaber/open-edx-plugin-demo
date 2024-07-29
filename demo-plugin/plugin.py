from openedx_events.learning.signals import SESSION_LOGIN_COMPLETED
from django.dispatch import receiver


print("Hello, world! from plugin.py")

@receiver(SESSION_LOGIN_COMPLETED)
def on_session_login_completed(sender, **kwargs):
    print("Session login completed")

