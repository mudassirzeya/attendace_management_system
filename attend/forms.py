from django.forms import ModelForm
from .models import Company, Attendance
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email', 'password1', 'password2')


class InternalUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['image']
