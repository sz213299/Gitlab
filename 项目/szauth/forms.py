from django import forms



from django.contrib.auth import get_user_model
class RegisterForm(forms.Form):
   username = forms.CharField()
   email = forms.EmailField(error_messages={'required': '请传入邮箱'})
   captcha = forms.CharField()
   password = forms.CharField(max_length=128)


   def clean_email(self):
       email = self.cleaned_data.get('email')

