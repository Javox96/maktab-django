from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegistForm(forms.ModelForm):
    """Ro'yxatdan o'tish formasi."""

    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput,
        label=_("Parol"),
    )
    confirm = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
        label=_("Parolni tasdiqlang"),
    )

    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': _("Foydalanuvchi nomi"),
        }

    def clean_username(self):
        """Username bandligini tekshirish."""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("Bu foydalanuvchi nomi allaqachon band!"))
        return username

    def clean_confirm(self):
        """Parollar bir xilligini tekshirish."""
        password = self.cleaned_data.get('password', '')
        confirm = self.cleaned_data.get('confirm', '')
        if password and confirm and password != confirm:
            raise forms.ValidationError(_("Parollar bir xil emas"))
        return confirm


class LoginForm(forms.Form):
    """Tizimga kirish formasi."""

    username = forms.CharField(
        max_length=128,
        label=_("Foydalanuvchi nomi"),
    )
    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput,
        label=_("Parol"),
    )
