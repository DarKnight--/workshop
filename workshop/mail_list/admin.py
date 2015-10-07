from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from mail_list import models
# Register your models here.


admin.site.register(models.Participant)