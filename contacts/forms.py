# Allows user to create a new contact and add it to the model
# Django creates form for me based off the model. 

from django import forms

from .models import Contact

class PostForm(forms.ModelForm):

     # Class Meta tells Django which model to create form for
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone_number')
