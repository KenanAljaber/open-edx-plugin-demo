from django.apps import AppConfig
class MyAppConfig(AppConfig):
    name = 'demo_plugin' # name of the module

    plugin_app = {
        'signals_config': {
            'lms.djangoapp': {
                'relative_path': 'plugin',
                'receivers': [{
                    'receiver_func_name': 'on_session_login_completed',
                    'signal_path': 'openedx_events.learning.signals.SESSION_LOGIN_COMPLETED',
                },
                {
                    'receiver_func_name': 'on_course_created',
                    'signal_path': 'openedx_events.content_authoring.signals.COURSE_CREATED',
                },
                {
                    'receiver_func_name': 'on_course_created',
                    'signal_path': 'openedx_events.learning.signals.COURSE_ENROLLMENT_CREATED',
                },
                
                
                ],
            }
        }
    }