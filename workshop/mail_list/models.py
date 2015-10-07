from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

emailValidation = RegexValidator(r'^[0-9_ a-z A-Z \-\.]+(@iitbhu\.ac\.in|@itbhu\.ac\.in)*$')
tenDigitContact = RegexValidator(r'^\d{10,10}$','Enter a Valid 10 digit number.', 'Invalid number')

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
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False, validators=[emailValidation])
    number = models.IntegerField(blank=False, validators=[tenDigitContact])
    other_number = models.IntegerField(blank=True, null=True, validators=[tenDigitContact])
    language = models.CharField(choices=LANGUAGE, max_length=10, blank=False)
    platform = models.CharField(max_length=5, choices=PLATFORM, blank=False)
