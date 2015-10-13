from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=2, null=True, blank=True)
    pop = models.CharField(max_length=25, null=True, blank=True)
    state_map = models.ImageField(upload_to='state_map', null=True, blank=True)
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    bird =models.CharField(max_length=255, null=True, blank=True)
    flag = models.ImageField(upload_to='flag', null=True, blank=True)
    statehood = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return '%s' % self.name


class StateCapital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    #state = models.ForeignKey('main.State', null=True, blank=True)
    #state = models.ManyToManyField('main.State', null=True, blank=True)
    state = models.OneToOneField('main.State', null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return '%s' % self.name


class City(models.Model):
    class Meta:
        verbose_name_plural = 'Cities'
    name = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey('main.State', null=True,blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    lon = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name


