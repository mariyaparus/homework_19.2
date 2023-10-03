from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word.lower() in cleaned_data:
                raise forms.ValidationError(f'Использование слова "{word}" в названии запрещено!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word.lower() in cleaned_data:
                raise forms.ValidationError(f'Использование слова "{word}" в описании продукта запрещено!')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
