from django import forms as f


class UserForm(f.Form):
    name = f.CharField(max_length=50)
    email = f.EmailField()
    age = f.IntegerField(min_value=0, max_value=120)

