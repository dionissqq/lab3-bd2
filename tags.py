import random
import string

tags = [
    'spam',
    'soup',
    'death',
    'raven',
    'bed',
    'food',
    'alch',
    'rabbit',
    'sql'
]

def get_random_tag_sequence():
    values = []
    for i in range(len(tags)):
        values.append(bool(random.getrandbits(1)))
    return dict(zip(tags, values))

def get_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

def get_random_user(arr):
    return random.choice(arr)
