"""Middleware that creates log records
for watched users"""
from askbot_log.models import UserLog

class LogActivityOfWatchedUsers(object):
    def process_response(self, request, response):
        user = request.user
        if request.method == 'POST' and user.is_authenticated() and user.is_watched():
            log = UserLog()
            log.ip_addr = request.META['REMOTE_ADDR']
            log.user = user
            data = request.POST.copy()
            data.pop('password', None)
            data.pop('password1', None)
            data.pop('password2', None)
            log.data = data
            log.save()
        return response
            
            

