from datetime import datetime, timedelta
import random
import string
import time
import names

from . import app

DATE_FORMAT = '%d/%m/%Y'

def get_random_letters(size=6):
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(size)])

def get_random_numbers(size=6):
    return ''.join([str(int(random.random() * 10)) for _ in range(size)])

def get_random_entry():
    return {
        'Equipe': get_random_letters().upper(),
        'NEFG': get_random_numbers(7),
        'NATT': get_random_numbers(),
        'Nom': names.get_last_name(),
        'Prénom': names.get_first_name(),
        'ABO': random.choice([*['A' for _ in range(50)], 'B', 'O']),
        'Date fin CIT': (datetime.today() + timedelta(days=random.random() * 20)).strftime(DATE_FORMAT),
        'MELD': get_random_numbers(2),
        'Score': int((random.random() * 10000)) / 10,
        'RgNet': get_random_numbers(1),
        'Note': '',
        'ALLOC': get_random_letters(4).upper(),
    }


@app.context_processor
def inject_user():
    return {
        'user': {
            'first_name': 'Damien',
            'last_name' : 'Savatier',
            'avatar_url': 'https://avatars3.githubusercontent.com/u/9400466?s=460&v=4',
        }
    }
