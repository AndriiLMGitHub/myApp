from django import forms
from .models import Add_item

class Add_item_post(forms.ModelForm):

    class Meta():
        model = Add_item
        fields = ('name_item', 'price_item', 'desciption_item', 'document', 'model_pic')
        widgets = {
            'name_item': forms.TextInput(attrs={'placeholder': 'Назва', 'class': 'form-control'}),
            'price_item': forms.TextInput(attrs={'placeholder': 'Ціна', 'class': 'form-control'}),
            'desciption_item': forms.Textarea(attrs={'placeholder': 'Текст', 'cols': 50, 'rows': 15, 'class':'form-control'})
        }
