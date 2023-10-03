from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
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


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # def clean_is_active(self):
    #     cleaned_data = self.cleaned_data['is_active']
    #     if cleaned_data:
    #         raise forms.ValidationError(
    #             f'У вас уже есть активная версия этого продукта.'
    #             f'Если вы хотите сделать активной эту версию, снимите флажок с предыдущей.')
    #     return cleaned_data
