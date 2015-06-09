from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User

class RequestLog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    filter_name = models.CharField(max_length=255)
    ip_addr = models.GenericIPAddressField()
    url = models.TextField()
    parameters = JSONField()
    session_key = models.CharField(max_length=40)
    session_data = JSONField()
    method = models.CharField(max_length=16)
    meta = JSONField()
    cookies = JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.user.username, self.ip_addr, self.url)
