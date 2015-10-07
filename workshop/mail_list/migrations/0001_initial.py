# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')])),
                ('number', models.IntegerField(validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('other_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$', b'Enter a Valid 10 digit number.', b'Invalid number')])),
                ('language', models.CharField(max_length=10, choices=[(b'Javascript', b'js'), (b'Python', b'python'), (b'Ruby', b'ruby'), (b'Java', b'java'), (b'C/C++', b'cpp')])),
                ('platform', models.CharField(max_length=5, choices=[(b'Windows App', b'wia'), (b'Linux/Terminal', b'li'), (b'Android App', b'ana'), (b'IOS App', b'ioa'), (b'Windows software', b'wi')])),
            ],
        ),
    ]
