from email.policy import default
from .models import ShippingAddress
from django import forms
import datetime

payment_methods =(
    ("Credit Card","Credit Card"),
    ("Debit Card","Debit Card"),
    ("PAYPAL","PAYPAL"),
    ("NETELLER","NETELLER"),
    ("Bank Transfer", "Bank Transfer"),
)

class form_shipping_information(forms.Form):
    name = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    last_name = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    email = forms.EmailField(required=True,max_length=100,widget=forms.EmailInput(attrs={'placeholder': 'Enter an email'}))
    address = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter a Address'}))
    city = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter a city'}))
    state = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter a state'}))
    postal_code = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter a Postal Code'}))
    payment_method = forms.ChoiceField(choices=payment_methods,required=True)
    
    def save_data(self, customer, order):
        order.transaction_id = datetime.datetime.now().timestamp()
        order.complete = True
        order.save()
        
        customer.payment_method = self.cleaned_data['payment_method']
        customer.save()
        
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = self.cleaned_data['address'],
            city = self.cleaned_data['city'],
            state = self.cleaned_data['state'],
            zipcode = self.cleaned_data['postal_code'],
        )
        
        print('*****'*5)
        print('Orden Completada y Direccion CREADA')
        print('*****'*5)