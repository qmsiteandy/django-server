from django import forms

class create_article_form(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

class login_form(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput) 