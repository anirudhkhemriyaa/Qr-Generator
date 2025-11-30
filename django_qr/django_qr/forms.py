from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50 , 
        label='Name',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter name of restaurant',
        })
        )
    url = forms.URLField(
        max_length=200 , 
        label='Menu_URl',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter URL of Menu(e.g. google-drive)',
        })
        )