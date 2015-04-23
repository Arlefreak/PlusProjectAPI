from django.db import models
from django.template import defaultfilters
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import os

def imgUpload(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class Project(models.Model):
    owner       = models.ForeignKey('auth.User', related_name='ProjectsOwned')
    name        = models.CharField('Name',max_length=140)
    description = models.TextField('Description')
    image       = models.ImageField('Image',upload_to=imgUpload)
    statusOpts  = (('pnd','Pending'),('pgr','Progress'),('tst','Testing'),('cls','Closed'))
    status      = models.CharField('Status',max_length=3,choices=statusOpts,default='pnd')
    client      = models.ForeignKey('Client', related_name='ProjectsClient')

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.owner)

class Task(models.Model):
    owner     = models.ForeignKey('auth.User', related_name='TasksOwned')
    name      = models.CharField('Name', max_length=140)
    status    = models.BooleanField('Status',default=False)
    date      = models.DateTimeField('ToDo Date')
    dateAdded = models.DateTimeField('Date added',auto_now_add=True)
    project   = models.ForeignKey('Project', related_name='TaskProjects')

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.owner)

class Payment(models.Model):
    owner       = models.ForeignKey('auth.User', related_name='PaymentsOwned')
    name        = models.CharField('Name',max_length=140)
    money       = models.FloatField('Money')
    typeOpts    = (('int','Initial'),('fnl','Final'),('otr','Other'))
    paymentType = models.CharField('Type', choices=typeOpts, max_length=3)
    date        = models.DateTimeField('Date completed')
    dateAdded   = models.DateTimeField('Date Added',auto_now_add=True)
    project     = models.ForeignKey('Project', related_name='PaymentProjects')
    taxPercentage = models.DecimalField('Tax Percentage',max_digits=5,decimal_places=2,validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
        ])

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.owner)

class Client(models.Model):
    owner = models.ForeignKey('auth.User', related_name='ClientsOwned')
    name  = models.CharField('Name',max_length=140)
    email = models.EmailField('Email',max_length=254)
    phone = models.CharField('Phone',max_length=140)
    image = models.ImageField('Image',upload_to=imgUpload)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.owner)
