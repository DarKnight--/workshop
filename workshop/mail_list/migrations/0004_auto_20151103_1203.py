# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_list', '0003_auto_20151007_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='language',
            field=models.CharField(blank=True, max_length=10, choices=[(b'js', b'Javascript'), (b'java', b'Java'), (b'ruby', b'Ruby'), (b'python', b'Python'), (b'cpp', b'C/C++')], error_messages={b'invalid': b'Please choose a language'}),
        ),
    ]
