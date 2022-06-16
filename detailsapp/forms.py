from django import forms
from detailsapp.models import Reviews


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Введите ваш Email'}),
            'comment': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Ваш отзыв', 'cols': 90, 'rows': 100}),
        }