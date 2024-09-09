from django.db import models
from django_neomodel import DjangoNode 
from neomodel import StringProperty, ArrayProperty, RelationshipTo, RelationshipFrom

# Create your models here.

class Person(DjangoNode):

    name = StringProperty()
    alias = ArrayProperty(StringProperty())
    date_of_birth = ArrayProperty(StringProperty())
    date_of_death = ArrayProperty(StringProperty())
    gender = StringProperty(choices=(
        ('male', 'male'), 
        ('female', 'female')
    ))

    father_of = RelationshipTo('Person', 'FATHER_OF')
    mother_of = RelationshipTo('Person', 'MOTHER_OF')

    class Meta:
        app_label = 'tree_view'

