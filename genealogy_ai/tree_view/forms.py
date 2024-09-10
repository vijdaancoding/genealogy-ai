from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'alias', 'date_of_birth', 'date_of_death', 'gender']
