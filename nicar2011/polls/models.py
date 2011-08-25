from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    active_flag = models.BooleanField()
    
    def __unicode__(self):
        return self.title

class Vote(models.Model):
    project = models.ForeignKey(Project)
    choice = models.IntegerField()
