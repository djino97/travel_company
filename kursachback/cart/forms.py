from django import forms
from db.models import Klient, Contract

TOURS_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 4)]
HOTELROOM_STARS = [(i, str(i)) for i in range(1, 6)]
PAYMENT = [('Yandex money', 'Yandex money'), ('PayPal', 'PayPal'), ('WebMoney', 'WebMoney'),
           ('Visa mastercard', 'Visa mastercard')]


class CartAddTourForm(forms.Form):
    quantity = forms.TypedChoiceField(label='количество', choices=TOURS_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    hotelroom = forms.TypedChoiceField(label='отель', choices=HOTELROOM_STARS, coerce=int)
    typeofpayment = forms.TypedChoiceField(label='вид оплаты', choices=PAYMENT, coerce=str)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['fio', 'dateofbirth', 'email', 'address', 'phone']
        labels = {
            'fio': 'ФИО',
            'dateofbirth': 'Дата рожденя',
            'address': 'Адрес',
            'phone': 'Ваш мобильный номер'
        }