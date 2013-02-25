from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.IntegerField()
