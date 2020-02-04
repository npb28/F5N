from django import forms

from .models import Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone_number')