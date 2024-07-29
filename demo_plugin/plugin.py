


print("Hello, world! from plugin.py updated")


def on_session_login_completed(user, **kwargs):
    print("Session login completed")
    print("Attributes and methods of user:")
    print(dir(user))



def on_course_created(course, **kwargs):
    print("Course created")
    print("Attributes and methods of course:")
    print(dir(course))


def on_course_enrollment_created(enrollment, **kwargs):
    print("Course enrollment created")
    print("Attributes and methods of enrollment:")
    print(dir(enrollment))

