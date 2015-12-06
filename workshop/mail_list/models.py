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
    language = models.CharField(choices=LANGUAGE, max_length=10, blank=True,
                                error_messages={'invalid':"Please choose a language"})
    platform = models.CharField(max_length=5, choices=PLATFORM, blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)+' : '+smart_unicode(self.number)+' : '+smart_unicode(self.email)


class Team(models.Model):
    team_name = models.CharField(max_length=50, blank=False, error_messages={'invalid':"Please enter your team name"})
    name_1 = models.CharField(max_length=50, blank=False, error_messages={'invalid':"Please enter a valid name"})
    name_2 = models.CharField(max_length=50, blank=False, error_messages={'invalid':"Please enter a valid name"})
    name_3 = models.CharField(max_length=50, blank=False, error_messages={'invalid':"Please enter a valid name"})
    name_4 = models.CharField(max_length=50, blank=False, error_messages={'invalid':"Please enter a valid name"})
    email_1 = models.EmailField(max_length=50, blank=False, validators=[emailValidation], unique=True,
                              error_messages={'invalid':"Please enter official e-mail address"})
    email_2 = models.EmailField(max_length=50, blank=False, validators=[emailValidation], unique=True,
                              error_messages={'invalid':"Please enter official e-mail address"})
    email_3 = models.EmailField(max_length=50, blank=False, validators=[emailValidation], unique=True,
                              error_messages={'invalid':"Please enter official e-mail address"})
    email_4 = models.EmailField(max_length=50, blank=False, validators=[emailValidation], unique=True,
                              error_messages={'invalid':"Please enter official e-mail address"})
    number_1 = models.IntegerField(blank=False, validators=[tenDigitContact],
                              error_messages={'invalid':"Please enter valid 10 digit number"})
    number_2 = models.IntegerField(blank=False, validators=[tenDigitContact],
                              error_messages={'invalid':"Please enter valid 10 digit number"})
    number_3 = models.IntegerField(blank=False, validators=[tenDigitContact],
                              error_messages={'invalid':"Please enter valid 10 digit number"})
    number_4 = models.IntegerField(blank=False, validators=[tenDigitContact],
                              error_messages={'invalid':"Please enter valid 10 digit number"})
    code_url = models.CharField(max_length=100, blank=False, error_messages={'invalid':"Please enter a valid url"})
    #language = models.CharField(choices=LANGUAGE, max_length=10, blank=True,
                                #error_messages={'invalid':"Please choose a language"})
    #platform = models.CharField(max_length=5, choices=PLATFORM, blank=True)

    def __unicode__(self):
        return smart_unicode(self.team_name)+' : '+smart_unicode(self.name_1)+' : '+smart_unicode(self.number_1)+' : '+smart_unicode(self.email_1)