from django import forms
from .models import AddPost

class AddPostForm(forms.ModelForm):
    class Meta:
        model = AddPost
        fields = ['head', 'description', 'images']  # Add the fields you want to include
