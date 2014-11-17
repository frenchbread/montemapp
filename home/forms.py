from django import forms
from models import Testers


class TestersForm(forms.ModelForm):

    class Meta:
        model = Testers
        fields = ['email']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control get-invite', 'placeholder': 'Email address here..'})
        }
