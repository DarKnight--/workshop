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




class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = '__all__'
        widgets = {
            'team_name' : forms.TextInput(attrs = {
                'placeholder' : "Max. 50 characters"
                }),
            'email_1' : forms.EmailInput(),
            'name_1'  :   forms.TextInput(),
            'number_1': forms.TextInput(),
            'email_2' : forms.EmailInput(),
            'name_2'  :   forms.TextInput(),
            'number_2': forms.TextInput(),
            'email_3' : forms.EmailInput(),
            'name_3'  :   forms.TextInput(),
            'number_3': forms.TextInput(),
            'email_4' : forms.EmailInput(),
            'name_4'  :   forms.TextInput(),
            'number_4': forms.TextInput(),
            'code_url' : forms.TextInput(attrs = {
                'placeholder' : ""
                }),
        }

    def clean_email(self):
        data = self.cleaned_data['email_1']
        if data:
            try:
                models.Team.objects.get(email_1=data)
            except models.Team.DoesNotExist:
                return data
            raise forms.ValidationError("The email is already registered")
        else:
            raise forms.ValidationError("e-mail field is mandatory")