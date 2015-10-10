from django.db import models
from django.core.validators import RegexValidator
from django.utils.encoding import smart_unicode
# Create your models here.

emailValidation = RegexValidator(r'^[0-9_ a-z A-Z \-\.]+(@iitbhu\.ac\.in|@itbhu\.ac\.in)*$')
tenDigitContact = RegexValidator(r'^\d{10,10}$')


class Participant(models.Model):
    LANGUAGE = {
            ('python', 'Python'),
            ('cpp', 'C/C++'),
            ('java', 'Java'),
            ('js', 'Javascript'),
            ('ruby', 'Ruby'),
    }
    PLATFORM = {
        ('li', 'Linux/Terminal'),
        ('wi', 'Windows software'),
        ('ana', 'Android App'),
        ('wia', 'Windows App'),
        ('ioa', 'IOS App')
    }
    name = models.CharField(max_length=50, blank=False, error_messages={'invalid':"Please enter your name"})
    email = models.EmailField(max_length=50, blank=False, validators=[emailValidation], unique=True,
                              error_messages={'invalid':"Please enter official e-mail address"})
    number = models.IntegerField(blank=False, validators=[tenDigitContact],
                              error_messages={'invalid':"Please enter valid 10 digit number"})
    other_number = models.IntegerField(blank=True, null=True, validators=[tenDigitContact],
                              error_messages={'invalid':"Please enter valid 10 digit number"})
    language = models.CharField(choices=LANGUAGE, max_length=10, blank=False,
                                error_messages={'invalid':"Please choose a language"})
    platform = models.CharField(max_length=5, choices=PLATFORM, blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)+' : '+smart_unicode(self.number)+' : '+smart_unicode(self.email)
