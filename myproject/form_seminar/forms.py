from django import forms as f


class RandomForm(f.Form):
    EVENT_CHOICES = [
        ('coin', 'Монета'),
        ('dice', 'Кости'),
        ('number', 'Числа'),
    ]
    event_type = f.ChoiceField(choices=EVENT_CHOICES, label='Выберите тип событий')
    attempts = f.IntegerField(min_value=1, max_value=64, label='Выберите количество попыток')
