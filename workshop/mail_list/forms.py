from django import forms
from mail_list import models
from django.shortcuts import HttpResponse


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = '__all__'
        widgets = {
            'email' : forms.EmailInput(),
            'name'  :   forms.TextInput(),
            'number': forms.TextInput(),
            'other_number': forms.TextInput(),
            'language': forms.RadioSelect(),
            'platform': forms.RadioSelect(),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if data:
            try:
                models.Participant.objects.get(email=data)
            except models.Participant.DoesNotExist:
                return data
            raise forms.ValidationError("The email is already registered")
        else:
            raise forms.ValidationError("e-mail field is mandatory")