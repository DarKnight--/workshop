# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mail_list', '0002_auto_20151005_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=50, unique=True, error_messages={b'invalid': b'Please enter official e-mail address'}, validators=[django.core.validators.RegexValidator(b'^[0-9_ a-z A-Z \\-\\.]+(@iitbhu\\.ac\\.in|@itbhu\\.ac\\.in)*$')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='language',
            field=models.CharField(max_length=10, choices=[(b'js', b'Javascript'), (b'java', b'Java'), (b'ruby', b'Ruby'), (b'python', b'Python'), (b'cpp', b'C/C++')], error_messages={b'invalid': b'Please choose a language'}),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=50, error_messages={b'invalid': b'Please enter your name'}),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number',
            field=models.IntegerField(error_messages={b'invalid': b'Please enter valid 10 digit number'}, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='other_number',
            field=models.IntegerField(blank=True, null=True, error_messages={b'invalid': b'Please enter valid 10 digit number'}, validators=[django.core.validators.RegexValidator(b'^\\d{10,10}$')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='platform',
            field=models.CharField(blank=True, max_length=5, choices=[(b'li', b'Linux/Terminal'), (b'ioa', b'IOS App'), (b'ana', b'Android App'), (b'wi', b'Windows software'), (b'wia', b'Windows App')]),
        ),
    ]
