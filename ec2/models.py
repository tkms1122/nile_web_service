from django.db import models

class Machine(models.Model):
    ''' A representation of instance.'''
    owner = models.CharField(max_length=256, default="") # owner's name
    name = models.CharField(max_length=256, default="") # machine's name
    core = models.PositiveIntegerField(default=1) # number of cpu cores
    memory = models.PositiveIntegerField(default=1) # memory (GB)
    status = models.PositiveIntegerField(default=0) # status

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
