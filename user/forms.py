import re
from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile


class RegisterForm(forms.Form):
    username = UsernameField(
        label="Tên đăng nhập",
        min_length=4,
        max_length=20,
        widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Tên đăng nhập', 'class': 'username'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'id': 'email', 'class': 'email', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        label="Mật khẩu",
        min_length=8,
        widget=forms.PasswordInput(attrs={'id': 'password1', 'class': 'password1', 'placeholder': 'Mật khẩu'})
    )
    password2 = forms.CharField(
        label="Nhập lại mật khẩu",
        min_length=8,
        widget=forms.PasswordInput(attrs={'id': 'password2', 'class': 'password2', 'placeholder': 'Nhập lại mật khẩu'})
    )

    error_messages = {
        'password_mismatch': 'Mật khẩu không hợp lệ',
        'username already exists': 'Tài khoản đã tồn tại',
        'Email already exists': 'Email đã tồn tại',
        "Username don't correct": 'Tên đăng nhập chứa kí tự không hợp lệ',
        'Tài khoản không tồn tại': 'Tài khoản không tồn tại',
    }

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'\W+$', username):
            raise forms.ValidationError(
                self.error_messages["Username don't correct"]
            )
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError(
                self.error_messages['username already exists'])
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError(
                self.error_messages['Email already exists'])
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch']
            )
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


# class LoginForm(forms.Form):
#     username = UsernameField(
#         label="Tên đăng nhập",
#         min_length=4,
#         max_length=20,
#         widget=forms.TextInput(attrs={'id': 'username', 'class': 'username', 'placeholder': 'Tên đăng nhập'})
#     )
#     password = forms.CharField(
#         label="Mật khẩu",
#         max_length=15,
#         widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'password', 'placeholder': 'Mật khẩu'})
#     )
#
#     error_messages = {
#         "Username don't correct": 'Tên đăng nhập không hợp lệ',
#         "Account don't correct": 'Tên đăng nhập và mật khẩu không đúng',
#     }
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data.get('password')
#         if re.search(r'\W+$', username):
#             raise forms.ValidationError(
#                 self.error_messages["Username don't correct"]
#             )
#         # my_user = authenticate(username=username, password=password)
#         # if my_user is None:
#         #     raise forms.ValidationError(
#         #         self.error_messages["Account don't correct"]
#         #     )
#         return username


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=False)

    # username = UsernameField(label='Tên đăng nhập', required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': _('Tên đăng nhập'),
        }


class UserUpdateForm1(forms.ModelForm):
    email = forms.EmailField(label='Email', required=False)

    # username = UsernameField(label='Tên đăng nhập', required=False)

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'img']
        labels = {
            'gender': _('Giới tính'),
            'img': _('Ảnh đại diện'),
        }
