from django import forms
from myapp.models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = "__all__"