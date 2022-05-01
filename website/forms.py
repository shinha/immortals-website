from django import forms

from .models import Application
from .models import MemberEntry
# import the built in form AND model
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class MemberEntryForm(forms.ModelForm):
    class Meta:
        model = MemberEntry
        fields = '__all__'