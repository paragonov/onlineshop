# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'input', }))
    from_email = forms.EmailField(label='Email', required=True,
                                  widget=forms.EmailInput(attrs={'placeholder': 'Ваш email', 'class': 'input', }))
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'placeholder': 'Оставьте комментарий', 'class': 'input', }),
                              required=True)
