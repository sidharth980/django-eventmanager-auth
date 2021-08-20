from django import forms
from .models import eventDetails

class eventForm(forms.ModelForm):
    class Meta:
        model = eventDetails
        fields = [
            'eventName',
            'eventDate',
            'eventDiscription'
        ]