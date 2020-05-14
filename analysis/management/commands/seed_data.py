import requests, traceback
from django.core.management import BaseCommand, CommandError
import pandas as pd
from analysis.models import Performance


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads performace data from github gist"
    def handle(self, *args, **options):
        try:
            URL = "https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/"  
            res = requests.get(url = URL)
            df = pd.read_html(res.text)[0]
            data = df.iloc[:,1:]
            Performance.objects.bulk_create(
                Performance(**vals) for vals in data.to_dict('records')
            )
        except:
            raise CommandError('Error with Seeding Data', traceback.format_exc())
