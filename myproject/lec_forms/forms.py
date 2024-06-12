import datetime

from django import forms as f


class UserForm(f.Form):
    name = f.CharField(max_length=50)
    email = f.EmailField()
    age = f.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise f.ValidationError('Name must be at least 3 characters')
        return name

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
            raise f.ValidationError('Email must end with vk.team or corp.mail.ru')
        return email


class ManyFieldsForm(f.Form):
    name = f.CharField(max_length=50)
    email = f.EmailField()
    age = f.IntegerField(min_value=18)
    height = f.FloatField()
    is_active = f.BooleanField(required=False)
    birthday = f.DateField(initial=datetime.date.today)
    gender = f.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsFormWidget(f.Form):
    name = f.CharField(max_length=50,
                       widget=f.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Введите имя пользователя'}))
    email = f.EmailField(widget=f.EmailInput(attrs={'class': 'form-control',
                                                    'placeholder': 'user@mail.ru'}))
    age = f.IntegerField(min_value=18, widget=f.NumberInput(attrs={'class': 'form-control'}))
    height = f.FloatField(widget=f.NumberInput(attrs={'class': 'form-control'}))
    is_active = f.BooleanField(required=False, widget=f.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthday = f.DateField(initial=datetime.date.today, widget=f.DateInput(attrs={'class': 'form-control',
                                                                                  'type': 'date'}))
    gender = f.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                           widget=f.RadioSelect(attrs={'class': 'form-check-input'}))
    message = f.CharField(widget=f.Textarea(attrs={'class': 'form-control'}))


class ImageForm(f.Form):
    image = f.ImageField()
