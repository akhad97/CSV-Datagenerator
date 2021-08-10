from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


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
    ('1', 'Double quote ("")'),
    ('2', 'quote ('')')
)

class Scheme(models.Model):
    upload = models.FileField(upload_to='', blank=True)
    name = models.CharField(max_length=30, blank=False)
    column_seperator = models.CharField(max_length=30, choices=TYPES, default="Dot Comma(;)")
    string_character = models.CharField(max_length=30, choices=TYPES1, default="Double quote("")")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    add_date = models.DateField(auto_now_add=True)

    type1 = models.CharField(max_length=30, choices=CHOICES, default="Select...")
    type2 = models.CharField(max_length=30, choices=CHOICES, default="Select...")
    type3 = models.CharField(max_length=30, choices=CHOICES, default="Select...")
    type4 = models.CharField(max_length=30, choices=CHOICES, default="Select...")
    type5 = models.CharField(max_length=30, choices=CHOICES, default="Select...")
    type6 = models.CharField(max_length=30, choices=CHOICES, default="Select...")
    

    col_name1 = models.CharField(max_length=30,  blank=True)
    col_name2 = models.CharField(max_length=30,  blank=True)
    col_name3 = models.CharField(max_length=30,  blank=True)
    col_name4 = models.CharField(max_length=30,  blank=True)
    col_name5 = models.CharField(max_length=30,  blank=True)
    col_name6 = models.CharField(max_length=30,  blank=True)

    order1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    order2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    order3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    order4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    order5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    order6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])

    # rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name + ' (' + str(self.author) + ')' + ' (id ' + str(self.id) + ')'

