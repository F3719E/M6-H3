from django import forms
from .models import ContactForm

# class ContactFormForm(forms.Form): #TODO DEFINE LOS CAMPOS DEL MODELO , CON SU TIPO DE CAMPO PREFORMATEADO DESDE DJANGO
#     customer_email = forms.EmailField(label='Email')
#     customer_name = forms.CharField(max_length=64, label='Nombre')
#     message = forms.CharField(label='Mensaje')
    
    
#     class ContactModelForm(forms.ModelForm):
#         class Meta:
#             model = ContactForm
#             fields = ['customer_email', 'customer_name', 'message']
            
class PostForm(forms.Form):
    customer_name = forms.CharField(max_length=64, label='Nombre'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.EmailField(label='Email'                 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje'                       , widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class PostFormModelForm(forms.ModelForm):
        class Meta:
            model = ContactForm
            fields = ['customer_email', 'customer_name', 'message']
            

class LoginPostForm(forms.Form):
    customer_name = forms.CharField(max_length=64, label='Nombre'   , widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.EmailField(label='Email'                 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje'                       , widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class LoginPostFormModelForm(forms.ModelForm):
        class Meta:
            model = ContactForm
            fields = ['customer_email', 'customer_name', 'message']