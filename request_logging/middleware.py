"""Middleware that creates log records
for watched users"""
from .models import RequestLog
from .conf import settings
from .utils import clean_dict, replace_dict_values, import_attribute
from django.conf import settings as django_settings
import inspect

class RequestLoggingMiddleware(object):
    def process_request(self, request):
        for test_filter in self.get_filters():
            callable_filter = self.get_callable_filter(test_filter)
            filter_name = self.get_filter_name(test_filter)
            if callable_filter(request):
                self.log_request(request, filter_name)
                return

    @classmethod 
    def get_filters(cls):
        #todo: get filters configurable via django admin
        return settings.REQUEST_LOGGING_FILTERS

    @classmethod
    def get_callable_filter(cls, path_or_filter):
        if callable(path_or_filter):
            return path_or_filter
        try: 
            return import_attribute(path_or_filter)
        except ImportError:
            ImproperlyConfigured(
                '{} is not an importable python path'.format(path_or_filter)
            )

    @classmethod
    def get_filter_name(cls, path_or_filter):
        if isinstance(path_or_filter, basestring):
            return path_or_filter
        elif inspect.isfunction(path_or_filter):
            funcname = path_or_filter.__name__
            module = inspect.getmodule(path_or_filter)
            if module:
                modname = module.__name__
                return '{}.{}'.format(modname, funcname)
            return funcname
        raise ImproperlyConfigured(
            'Invalid filter {}, must be dotted path'
            'or function'.format(unicode(path_or_filter))
        )

    @classmethod
    def log_request(cls, request, filter_name):
        """logs request data"""
        log = RequestLog()
        log.filter_name = filter_name
        log.ip_addr = request.META['REMOTE_ADDR']
        user = getattr(request, 'user', None)
        if user.is_authenticated():
            log.user = user
        log.url = request.path
        parameters = clean_dict(request.REQUEST)
        replace_dict_values(
            parameters,
            settings.REQUEST_LOGGING_HIDE_PARAMETERS,
            '********'
        )
        log.parameters = parameters
        log.session_key = request.session.session_key
        log.session_data = clean_dict(request.session)
        log.method = request.method
        log.meta = clean_dict(request.META)
        log.cookies = clean_dict(request.COOKIES)
        log.save()
