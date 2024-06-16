from django import forms
from django.utils import timezone


def get_today_string():
    return timezone.localtime(timezone.now()).strftime('%d.%m.%Y')


class CompanyForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=200,
        required=True
    )
    inn = forms.CharField(
        label='ИНН',
        max_length=10,
        min_length=10,
        required=True
    )
    creation_date = forms.DateField(
        label='Дата создания',
        input_formats=('%Y-%m-%d',),
        widget=forms.TextInput(attrs={'type': 'date'}),
        initial=get_today_string,
        required=True
    )


class ProductForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=200,
        required=True
    )
    description = forms.CharField(
        label='Описание',
        max_length=2000,
        required=True
    )
    price = forms.FloatField(
        label='Цена',
        min_value=0,
        step_size=0.1
    )
