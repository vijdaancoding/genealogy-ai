from django.core.management.base import BaseCommand, CommandParser
from django.conf import settings
from tree_view.models import Person

class Command(BaseCommand):
    help = 'For importing sample family tree and connect with your NEO4J database'

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str, help='Neo4j connection URL (e.g., bolt://<username>:<password>@localhost:7687)')
    
    def handle(self, **options):

        neo4j_url = options['url']

        if not neo4j_url:
            self.stdout.write(self.style.ERROR('ERROR: Please specify the URL using --url'))
            return

        settings.NEOMODEL_NEO4J_BOLT_URL = neo4j_url

        self.stdout.write(self.style.SUCCESS(f'Connecting to Neo4j at {neo4j_url}...'))

        try:
            # People
            root_person = Person(name='Hazrat Muhammad', 
                                alias=['Ahmad', 'Mustafa', 'Al-Amin', 'Al-Sadiq', 'Seal of Prophets'],
                                date_of_birth=["??-??-0570", "12th Rabi-ul-Awal"],
                                date_of_death=["??-??-0632", "12th Rabi-ul-Awal, 11 A.H"],
                                gender='male').save()
            
            fatima = Person(name='Hazrat Fatimah',
                            alias=['Zahra', 'Saddiqah', 'Batool', 'Masoomah', 'Syeda'],
                            date_of_birth=["??-??-0605", "20th Jumada-al-Thani"],
                            date_of_death=["??-??-0632", "13th Jamadi-ul-Awwal, 11 A.H"],
                            gender='female').save()
            
            ali = Person(name='Hazrat Ali',
                        alias=['Siddiq', 'Wali', 'Amir Al-Muminin', 'Wasi'],
                        date_of_birth=['17-03-0599', '13th Rajab'],
                        date_of_death=['27-01-0661', '21st Ramadan, 40 A.H'],
                        gender='male').save()
            
            hussain = Person(name='Hazrat Hussain',
                        alias=['Aba Abd Allah', 'Shabbir'],
                        date_of_birth=['11-01-0626', '3rd Shaban, 3 A.H'],
                        date_of_death=['10-10-0680', '10th Muharram, 61 A.H'],
                        gender='male').save()
            
            # Relationship

            root_person.father_of.connect(fatima)
            ali.husband_of.connect(fatima)
            ali.father_of.connect(hussain)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'ERROR: {e}'))
