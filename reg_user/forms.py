from django import forms

class RegsitrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    website = forms.URLField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Website address'}))
    company = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Company name'}))
    address = forms.CharField(
        label='Unit',
        widget=forms.TextInput(attrs={'placeholder': 'Appartment/Unit'})
    )
    street_number = forms.CharField()
    street_name = forms.CharField(label='Street name')
    city = forms.CharField()
    state = forms.CharField(label='State/Province')
    zip_code = forms.CharField(label='Zip/Postal code')
    country = forms.CharField()
