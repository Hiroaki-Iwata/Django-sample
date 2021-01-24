from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','quantity','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例:りんご'}),
                    'quantity': forms.NumberInput(attrs={'min':1}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
