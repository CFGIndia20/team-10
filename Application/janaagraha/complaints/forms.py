from .models import Complaints
from django import forms 

class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ("Topic","location")
