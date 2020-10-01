from django import forms
from .models import todos
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class listform(forms.ModelForm):
    class Meta:
        model = todos
        fields = ["title","description","finished","date"]

class UserLogin (forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('does ot exist')
            if not user.check_password(password):
                raise forms.ValidationError('incorrect')
            if not user.is_active:
                raise forms.ValidationError('not active')
        return super(UserLogin, self).clean(*args,**kwargs)

class UserRegister(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=[
            "username",
            "email",
            "password"
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("used")
        return email