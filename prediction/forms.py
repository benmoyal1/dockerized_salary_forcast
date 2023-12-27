from django import forms
from .models import LinearRegressionModel


class LinearRegressionModelForm(forms.ModelForm):
    class Meta:
        model = LinearRegressionModel
        fields = ['country', 'education', 'years_of_education']
