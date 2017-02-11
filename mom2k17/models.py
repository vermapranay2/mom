from django.core.validators import RegexValidator
from django.db import models
from multiselectfield import MultiSelectField
from django.shortcuts import render
from django.core.urlresolvers import reverse


# Create your models here.
class Info(models.Model):
    email=models.EmailField(max_length=220,)

    def __str__(self):
        return str(self.email)

    def __unicode__(self):
        return str(self.email)


class Register(models.Model):
    EVENTS = (('TME', 'Technical Model Exhibition'),
              ('IIP', 'Brainwave'),
              ('QUIZ', 'Quiz'),
              ('APP', 'Apps Corner'),
              ('Flash', 'Flash'),
              ('OSD', 'Creations'))
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=50,)
    city = models.CharField(max_length= 50,)
    address = models.TextField(max_length=2000,)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10,)  # validators should be a list
    institute = models.CharField(max_length=1000,)
    # event = models.TextField(max_length=1000, default="pranay")
    event = MultiSelectField(choices=EVENTS,max_choices=6,max_length=100)
    message = models.TextField(max_length=2000,  blank=True)
    momid = models.CharField(max_length=15, default='MOM2K17-000')


    def get_absolute_url(self ):
        return reverse('home')
    def __str__(self):
        return str(self.pk)+ str(self.name)



class School(models.Model):

    name = models.TextField(max_length=1000, )
    address = models.TextField(max_length=2000)
    email = models.EmailField(max_length=254, )
    principal = models.TextField(max_length=254, )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number_principal = models.CharField(validators=[phone_regex], max_length=10)  # validators should be a list
    incharge = models.TextField(max_length=254,)
    phone_regex2 = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number_incharge = models.CharField(validators=[phone_regex2], max_length=10)
    message = models.TextField(max_length=2000)
    momid = models.TextField(max_length=15, default='MOM2K17sc-000')



