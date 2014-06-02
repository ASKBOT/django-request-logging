from django.db import models
from picklefield.fields import PickledObjectField
from askbot.models import User

class UserLog(models.Model):
    user = models.ForeignKey(User)
    ip_addr = models.GenericIPAddressField()
    data = PickledObjectField()
