#handling forms to be displayed to the users in html
from django.forms import ModelForm
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['recieved_quantity']
#the above form is edited by the workers 

class Saleform(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_recieved','issued_to','branch_name']