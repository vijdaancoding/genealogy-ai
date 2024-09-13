from django.db import models
from django_neomodel import DjangoNode 
from neomodel import StringProperty, ArrayProperty, RelationshipTo, RelationshipFrom

# Create your models here.

class Person(DjangoNode):

    name = StringProperty()
    alias = ArrayProperty()
    date_of_birth = ArrayProperty()
    date_of_death = ArrayProperty()
    gender = StringProperty()

    father_of = RelationshipTo('Person', 'FATHER_OF')
    son_of = RelationshipFrom('Person', 'FATHER_OF')
    mother_of = RelationshipTo('Person', 'MOTHER_OF')
    daughter_of = RelationshipFrom('Person', 'MOTHER_OF')
    husband_of = RelationshipTo('Person', 'HUSBAND_OF')
    wife_of = RelationshipFrom('Person', 'WIFE_OF')

    class Meta:
        app_label = 'tree_view'

