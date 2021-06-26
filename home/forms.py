from django import forms
from .models import Post,Category,Profile, Comment
from django.contrib.auth.models import User,auth

from froala_editor.widgets import FroalaEditor




choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    body = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Post
        fields = ('title','author','category','body','header_image')  
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','placeholer':'username','id':'temp', 'value':'','type':'hidden' ,}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices = choices ,attrs={'class':'form-control'}),
            

        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','website_url','instagram_url')
        widgets = {
            'bio' :  forms.Textarea(attrs={'class':'form-control'}),
           # 'profile_pic' : forms.ImageField(),
            'website_url': forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')  
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholer':'username','id':'temp', 'value':'','type':'hidden' ,}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }