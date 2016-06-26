from django.conf import settings
from django.db import models

class IP(models.Model):
    address = models.PositiveIntegerField()
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return "IP"

class Machine(models.Model):
    ''' A representation of instance.'''
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    machine_token = models.CharField(unique=True, max_length=256)
    name = models.CharField(max_length=256, default="") # machine's name
    core = models.PositiveIntegerField(default=1) # number of cpu cores
    memory = models.PositiveIntegerField(default=1) # memory (GB)
    status = models.PositiveIntegerField(default=0) # status
    ip = models.OneToOneField(IP)

    STATUS = {
            0: 'Stopped',
            1: 'Running',
            2: 'Resumed'
    }

    STATUSCOLOR = {
            0: 'badge-gray',
            1: 'badge-green',
            2: 'badge-yellow'
    }

    def __str__(self):
        return "machine"

    def getstate(self):
        return self.STATUS[self.status]

    def getstatecolor(self):
        return self.STATUSCOLOR[self.status]

# Create your models here.
