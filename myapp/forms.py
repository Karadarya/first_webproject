from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'public_post', 'published_date', 'scores')


class RegisterForm(UserCreationForm) :
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

"""#username = forms.CharField(max_length=30)
	#password1=forms.CharField(max_length=30, widget=forms.PasswordInput())
	#password2=forms.CharField(max_length=30, widget=forms.PasswordInput())
    class Meta:
            model = User
	    fields = ('username', 'password1', 'password2')


	def check_username(self):
	    try: User.objects.get(username=self.cleaned_data['username'])
	    except User.DoesNotExist : return self.cleaned_data['username']
	    raise forms.ValidationError("Username already exists")


	def check_pass(self):
	    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data: if self.cleaned_data['password1'] != self.cleaned_data['password2']: raise forms.ValidationError("Passwords don't match")
	    return self.cleaned_data


	def save(self): # create new user
	    new_user=User.objects.create_user(username=self.cleaned_data['username'],
		                            password=self.cleaned_data['password1'],
		                            email=self.cleaned_data['email'],
		                                )

	    return new_user


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')

	def save(self, commit = True):
	   user = super(RegisterForm, self).save(commit = False)
	   if commit: user.save()
	   return user"""
