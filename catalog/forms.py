from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.constants import forbidden_words
from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"

        self.fields['price'].widget.attrs.update({
            'placeholder': 'Цена продукта должна быть положительным числом!'
        })


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']

    def clean_name(self):
        product_name = self.cleaned_data.get('name')
        for forbidden_word in forbidden_words:
            if forbidden_word in product_name.lower():
                raise ValidationError(f"Нельзя указывать данное слово {product_name}.")
        return product_name

    def clean_description(self):
        product_description = self.cleaned_data.get('description')
        for forbidden_word in forbidden_words:
            if forbidden_word in product_description.lower():
                raise ValidationError(f"Нельзя указывать запрещённое слово {product_description}.")
        return product_description

    def clean_price(self):
        product_price = self.cleaned_data.get('price')
        if product_price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return product_price
