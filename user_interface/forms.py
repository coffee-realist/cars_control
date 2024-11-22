from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """
    Форма для регистрации пользователей.
    Добавляет поля для подтверждения пароля и настройки их атрибутов.
    """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Пароль"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Подтверждение пароля"
    )

    class Meta:
        """
        Метаданные формы:
        - Связана с моделью User.
        - Использует стандартные поля, включая username, email и пароль.
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Проверяет совпадение паролей. Если пароли не совпадают, добавляется ошибка.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            self.add_error('password_confirm', "Пароли не совпадают.")
        return cleaned_data

    def save(self, commit=True):
        """
        Сохраняет пользователя, устанавливая хэшированный пароль.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
