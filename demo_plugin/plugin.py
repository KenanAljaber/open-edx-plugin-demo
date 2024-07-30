from .api import post
from datetime import datetime


import logging

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Set the format of the log messages
    handlers=[
        logging.StreamHandler()  # Output logs to the console
    ]
)


logger = logging.getLogger('myapp')
SITE_URL=""

logger.debug("site url is ")
logger.debug(SITE_URL)
print("Hello, world! from plugin.py with tenant")

def on_session_login_completed(user, **kwargs):
    print("Session login completed")
    print("Attributes and methods of user:")
    print(user)



def on_course_created(course, **kwargs):
    print("Course created")
    print("Attributes and methods of course:")
    print(course)


def on_certificate_created(certificate, **kwargs):
    print("Certificate created")
    print(certificate)


def on_certificate_awarded(certificate, **kwargs):
    print("Certificate awarded")
    print(certificate)


def on_course_enrollment_created(enrollment, **kwargs):
    logger.debug("Course enrollment created")
    print("Attributes and methods of enrollment:")
    print(enrollment)


    enrollment_data = {
        'user': {
            'id': enrollment.user.id,
            'is_active': enrollment.user.is_active,
            'username': enrollment.user.pii.username,
            'email': enrollment.user.pii.email,
            'name': enrollment.user.pii.name
        },
        'course': {
            'course_key': str(enrollment.course.course_key),  
            'display_name': enrollment.course.display_name,
            'start': enrollment.course.start.isoformat() if enrollment.course.start else None,
            'end': enrollment.course.end.isoformat() if enrollment.course.end else None
        },
        'mode': enrollment.mode,
        'is_active': enrollment.is_active,
        'creation_date': enrollment.creation_date.isoformat() if isinstance(enrollment.creation_date, datetime) else enrollment.creation_date,
        'created_by': enrollment.created_by,
        "source": SITE_URL,
        "type":"enrollment"
    }

 
    api_url = "https://dev.api.eduflix.com.ec/api/notifications/create"

    
    post(api_url, enrollment_data)