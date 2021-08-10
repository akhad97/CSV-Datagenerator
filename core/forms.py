from django import forms
from .models import *



class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = [
            'name', 'column_seperator', 'string_character', 'col_name1', 'col_name2', 'col_name3', 'col_name4', 'col_name5', 'col_name6',
            'type1', 'type2', 'type3', 'type4', 'type5', 'type6',
            'order1', 'order2', 'order3', 'order4', 'order5', 'order6',
        ]

        labels = {
            'name': 'Name', 'column_seperator': 'Column Seperator', 'string_character': 'String Character', 'col_name1': 'Column Name', 'col_name2': 'Column Name', 'col_name3':'Column Name',
            'col_name4':'Column Name', 'col_name5': 'Column Name', 'col_name6': 'Column Name', 'type1': 'Type', 'type2':'Type',
            'type3':'Type', 'type4':'Type', 'type5':'Type', 'type6':'Type', 'order1':'Order', 'order2':'Order', 'order3':'Order',
            'order4':'Order', 'order5':'Order', 'order6':'Order'
        }