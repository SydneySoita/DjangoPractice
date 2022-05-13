from django import forms
from second_app.models import User


class My_Model_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
