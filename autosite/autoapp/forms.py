from django import forms
from .models import Car
from django.db import models

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['class_type', 'make', 'model', 'seats', 'doors', 'license_plate', 'has_ac', 'transmission', 'daily_rate', 'base_price', 'mileage']
        labels = {
            'class_type': 'Номер класса автомобиля',
            'make': 'Марка',
            'model': 'Модель',
            'seats': 'Места',
            'doors': 'Двери',
            'license_plate': 'Номер',
            'has_ac': 'Кондиционер',
            'transmission': 'Трансмиссия',
            'daily_rate': 'Стоимость в день',
            'base_price': 'Базовая стоимость',
            'mileage': 'Прокат',
        }
        widgets = {
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'doors': forms.NumberInput(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'has_ac': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'daily_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
        }