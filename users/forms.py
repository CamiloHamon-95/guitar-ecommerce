from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from payments.models import Customer

countries =(
    ("AR", "Argentina"),
    ("BR", "Brasil"),
    ("COL", "Colombia"),
    ("ECU", "Ecuador"),
    ("CH", "Chile"),
)

class form_signup(forms.Form):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Create a Username'}),)
    first_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}),)
    last_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}),)
    password = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}))
    password_confirm = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm a password'}))
    date_birth = forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={'type': 'date'}))
    id_card = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Digit your ID'}),)
    address = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}),)
    email = forms.EmailField(min_length=6,max_length=100,widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    country = forms.ChoiceField(choices=countries,required=False)
    city = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder': 'Enter your City'}),)
    province = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder': 'Enter your Province'}),)
    postal_code = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Enter your ZipCode'}),)
    phone = forms.CharField(max_length=15,required=False,widget=forms.TextInput(attrs={'placeholder': 'Digit your phonenumber'}),)
    picture = forms.ImageField()
    save_info = forms.BooleanField(required=False)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username
    
    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirm = data['password_confirm']
        
        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match')
        
        return data
    
    def save_data(self):

        for key, value in self.cleaned_data.items():
            if value is None:
                if key in ['id_card', 'postal_code']:
                    self.cleaned_data[key] = 0
                else:
                    self.cleaned_data[key] = ''
        # --> User attributes <--
        newUser = User.objects.create_user(
            username = self.cleaned_data['username'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password']
        )
        
        # --> Customer attributes <--
        myCustomer = Customer(user=newUser)
        myCustomer.name = self.cleaned_data['first_name']
        myCustomer.email = self.cleaned_data['email']
        myCustomer.save()
        
        # --> Profile attributes <--
        myprofile = Profile(user=newUser)
        myprofile.id_card = self.cleaned_data['id_card']
        myprofile.address = self.cleaned_data['address']
        myprofile.country = self.cleaned_data['country']
        myprofile.city = self.cleaned_data['city']
        myprofile.province = self.cleaned_data['province']
        myprofile.postal_code = self.cleaned_data['postal_code']
        myprofile.phone = self.cleaned_data['phone']
        myprofile.picture = self.cleaned_data['picture']
        myprofile.date_birth = self.cleaned_data['date_birth']
        myprofile.save()
        
class form_login(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Username or Email'}),
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
    )