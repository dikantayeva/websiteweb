from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import UserProfile


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DetailForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DetailForm, self).__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['iin'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg form-control-alt'

        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['iin'].widget.attrs['placeholder'] = 'IIN'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = UserProfile
        fields = ['phone', 'iin', 'email']
