from django import forms


class SignUpForm(forms.Form):
    merchant_name = forms.CharField(max_length=100,label='Merchant Name',required=True)
    merchant_user_name = forms.CharField(max_length=50,label='Merchant Username',required=True)
    merchant_email = forms.EmailField(max_length=50, label='Merchant Email',required=True)
    merchant_password = forms.CharField(max_length=50,widget=forms.PasswordInput,label='Merchant Password',required=True)
    merchant_confirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput,label='Merchant Confirm Password',required=True)
    merchant_address = forms.CharField(max_length=500,widget=forms.Textarea,label='Merchant Address',required=True)
    merchant_redirect_url = forms.URLField(max_length=100,label='Merchant Redirect URL',required=True)

    def clean(self):
        form_data = self.cleaned_data
        if(form_data.get('merchant_password') != form_data.get('merchant_confirm_password')):
            self._errors['merchant_password'] = ["Password does not match"]
            del form_data['merchant_password']
            del form_data['merchant_confirm_password']
        return form_data





