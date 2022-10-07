import csv

from foodgram import settings
from django.core.management import BaseCommand
from recipes.models import Recipe
from users.models import User

MODELS_FILES = {
    User: 'users.csv',
   # Recipe: 'recipes.csv'
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model, file in MODELS_FILES.items():
            with open(
                    f'{settings.BASE_DIR}/data/{file}',
                    'r', encoding='utf-8',
            ) as table:
                reader = csv.DictReader(table)
                model.objects.bulk_create(model(**data) for data in reader)

        self.stdout.write(self.style.SUCCESS(
            '=== Тестовые данные успешно загружены ===')
        )
