from django import forms
from modelform.model import Register


class Majina(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        widgets = {'Firstname': forms.TextInput(attrs={'placeholder': 'Enter Firstname'}),
                   'Lastname': forms.TextInput(attrs={'placeholder': 'Enter Lastname'})
                   }
