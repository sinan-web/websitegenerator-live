from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
  
class CustomerData(forms.ModelForm):
  
    class Meta:
        model = CustomerData
        fields = ["customerName", "template", "companyName","aboutUsText", "image1", "image2", "image3", "adress", "telephone", "email"]

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

# class TemplateSelection(forms.Form):
#     CHOICES=[("template1", "template2", "template3")]
#     template = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

# class SelectedTemplate(forms.ModelForm):
#     class Meta:
#         model = TemplateSelection
#         fields = "__all__"