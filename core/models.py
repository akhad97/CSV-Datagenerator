from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model


CHOICES = (

    ('1', 'Select...'),
    ('2', 'string'),
    ('3', 'int'),
    ('4', 'bool'),
    ('5', 'list'),
    ('6', 'float'),
    ('7', 'tuple')
)

TYPES = (
    ('1', 'Dot comma (;)'),
    ('2', 'Comma (,)')
)

TYPES1 = (
    ('1', "Double quote ("")"),
    ('2', "quote ('')")
)

class Scheme(models.Model):
    upload = models.FileField(upload_to='', blank=True)
    name = models.CharField(max_length=30, blank=False)
    column_seperator = models.CharField(max_length=30, choices=TYPES, default="Dot Comma(;)")
    string_character = models.CharField(max_length=30, choices=TYPES1, default="Double quote("")")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    add_date = models.DateField(auto_now_add=True)   

    type = models.CharField(max_length=30, blank=True, choices=CHOICES)
    type2 = models.CharField(max_length=30, blank=True, choices=CHOICES)
 
    col_name = models.CharField(max_length=30, blank=True)
    col_name2 = models.CharField(max_length=30, blank=True)
    
    order = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(9)])
    order2 = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(9)])
    rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.name + ' (' + str(self.author) + ')' + ' (id ' + str(self.id) + ')'

    

