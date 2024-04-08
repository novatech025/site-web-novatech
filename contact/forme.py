from django import forms
from . import models


# class commentaireform(forms.ModelForm):
    
#     class Meta:
        
#         model = models.utilisateures
#         forms.error_css_class = 'error'
#         forms.required_css_class = "required"
#         fields = "__all__"


class commentaireform(forms.Form):
    name = forms.CharField(max_length = 30, label='' ,widget=forms.TextInput(attrs={
        'class':'nom'
    }))
    email = forms.EmailField(label='' ,widget=forms.EmailInput(attrs={
        'class':'mail'
    }))
    message = forms.CharField( label='' ,widget=forms.Textarea(attrs={
        'class':'message'
    }))