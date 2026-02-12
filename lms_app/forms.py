from django import forms
from .models import *
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['title',
                'author',
                'photo_book',
                'photo_author',
                'price', 
                'rental_price_day',
                'rental_period',
                'total_rental',
                'pages', 
                'category', 
                'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class': 'form-control','id':'rentalprice'}),
            'rental_period': forms.NumberInput(attrs={'class': 'form-control', 'id':'rentaldays'}),
            'total_rental': forms.NumberInput(attrs={'class': 'form-control' ,'id':'totalrental'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control-file'}),
            'photo_author': forms.FileInput(attrs={'class': 'form-control-file'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            
            }
