from django import forms
from django.db.models.expressions import Col
from django.forms.formsets import formset_factory
from .models import *

class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = [
            'column_seperator',
            'string_character',
            'name', 

            'col_name',
            'col_name2',
           
            
            'type',
            'type2', 
           
            
            'order', 
            'order2', 
             
        ]

        labels = {
            'name': 'Name',  
            'col_name': 'Column Name', 
            'col_name2': 'Column Name', 
           

            'type': 'Type', 
            'type2':'Type',
          

            'order':'Order', 
            'order2':'Order', 
         
        }

