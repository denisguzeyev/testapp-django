# TODO: Implement your user forms here


from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=255)
    password1 = forms.CharField(label='Password1', max_length=255)
    password2 = forms.CharField(label='Password2', max_length=255)