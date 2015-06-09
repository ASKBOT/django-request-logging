from django.conf import settings
from appconf import AppConf

class RequestLoggingConf(AppConf):
    FILTERS = ()
    HIDE_PARAMETERS = ()

    class Meta:
        prefix = 'request_logging'
