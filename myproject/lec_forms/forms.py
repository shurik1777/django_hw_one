import datetime

from django import forms as f


class UserForm(f.Form):
    name = f.CharField(max_length=50)
    email = f.EmailField()
    age = f.IntegerField(min_value=0, max_value=120)


class ManyFieldsForm(f.Form):
    name = f.CharField(max_length=50)
    email = f.EmailField()
    age = f.IntegerField(min_value=18)
    height = f.FloatField()
    is_active = f.BooleanField(required=False)
    birthday = f.DateField(initial=datetime.date.today)
    gender = f.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
