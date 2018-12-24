from django import forms
from webapp.models import Food, Order, OrderFood


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address', 'contact_phone', 'contact_name', 'operator', 'courier']


class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = ['order']
