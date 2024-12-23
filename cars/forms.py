from django import forms
from .models import Car, Comment


class CarForm(forms.ModelForm):
    """
    Форма для управления моделью Car (создание и редактирование).
    """
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class CommentForm(forms.ModelForm):
    """
    Форма для добавления комментариев к машине.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
