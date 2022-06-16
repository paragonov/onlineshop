from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'city', 'address', 'postal_code', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input', 'placeholder': 'Ваше Имя'}),
            'last_name': forms.TextInput(attrs={'class':'input', 'placeholder': 'Ваша фамилия'}),
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class':'input', 'placeholder': 'Ваш адрес'}),
            'postal_code': forms.NumberInput(attrs={'class':'input', 'placeholder': 'Почтовый индекс'}),
            'city': forms.TextInput(attrs={'class':'input', 'placeholder': 'Город'}),
            'comment': forms.Textarea(attrs={'class':'input', 'placeholder': 'Ваш комментарий'}),
        }
