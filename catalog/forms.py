from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-basic'
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs['class'] = 'form-control datepicker'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-time'
            elif isinstance(field.widget, forms.widgets.SelectMultiple):
                field.widget.attrs['class'] = 'form-control select2 select2-multiple'
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = 'form-control select2'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Использование слова "{word}" в названии запрещено!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Использование слова "{word}" в описании продукта запрещено!')
        return cleaned_data

    # def clean(self):
    #     cleaned_data = super().clean()
    #     word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #
    #     for key in cleaned_data.keys():
    #         for word in word_list:
    #             if word in cleaned_data[key].lower():
    #                 raise forms.ValidationError(f'Использование слова "{word}" в {key} запрещено!')
    #
    #     return cleaned_data


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

    # def clean(self):
    #     super().clean()
    #     product_versions_list = []
    #     for form in Product.objects.get(pk=self.cleaned_data['product'].pk).formset:
    #         product_versions_list.append(form.cleaned_data['is_active'])
    #         if product_versions_list.count(True) > 1:
    #             raise forms.ValidationError('Уже есть активная версия')
