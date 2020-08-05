from blog.models import Comment
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class CommentForm(ModelForm):
    class Meta:
        #contents = forms.CharField(max_length=4000, required=True)
        model = Comment
        fields = ['contents']




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']








class RawProductForm(forms.Form):
    title = forms.CharField()
    desc  = forms.CharField()
    price = forms.DecimalField()
