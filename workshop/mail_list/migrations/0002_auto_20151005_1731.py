# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='language',
            field=models.CharField(max_length=10, choices=[(b'js', b'Javascript'), (b'java', b'Java'), (b'ruby', b'Ruby'), (b'python', b'Python'), (b'cpp', b'C/C++')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='platform',
            field=models.CharField(max_length=5, choices=[(b'li', b'Linux/Terminal'), (b'ioa', b'IOS App'), (b'ana', b'Android App'), (b'wi', b'Windows software'), (b'wia', b'Windows App')]),
        ),
    ]
