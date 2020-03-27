from django import forms
from .models import comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']

class CommentForm(forms.ModelForm):
	comment_content = forms.CharField(max_length=500)
	class Meta:
		model = comment
		fields = ['comment_content']