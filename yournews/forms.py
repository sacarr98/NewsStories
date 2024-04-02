from django import forms
from .models import News, Profile, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Profile picture form
class ProfilePicForm(forms.ModelForm):
    #profile_image = forms.CloudinaryField(label="Profile Picture")#
    profile_bio = forms.CharField(label="Profile Bio", max_length=100, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Bio'}))
    website_link = forms.CharField(label="Website", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Website'}))
    facebook_link = forms.CharField(label="Facebook", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Facebook'}))
    instagram_link = forms.CharField(label="Instagram", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Instagram'}))

    class Meta:
        model = Profile
        fields = ('profile_image', 'profile_bio', 'website_link', 'facebook_link', 'instagram_link')


#News Form
class NewsForm(forms.ModelForm):
    title = forms.CharField(required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder":"News Title",
                "class":"form-control",
            }
        ),
        label="",
        )
    summary = forms.CharField(required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder":"Summarise Your News",
                "class":"form-control",
            }
        ),
        label="",
        )
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Share Your News",
                "class":"form-control",
            }
        ),
        label="",
        )
    class Meta:
        model = News
        exclude = ("user", "likes",)


# Comment Form
class CommentForm(forms.ModelForm):
    comment_body = forms.CharField(required=True, 
        label="", max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Comment'}))
    class Meta:
        model = Comment
        fields = ('comment_body',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'