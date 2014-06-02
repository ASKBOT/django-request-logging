from django.db import models
from picklefield.fields import PickledObjectField
from askbot.models import User

class UserLog(models.Model):
    user = models.ForeignKey(User)
    ip_addr = models.GenericIPAddressField()
    url = models.TextField()
    data = PickledObjectField()

    def __unicode__(self):
        return u'%s %s %s' % (self.user.username, self.ip_addr, self.url)
