import re
from meeter.models import *


def valid_register(qwery):
    valid = True
    login_pattern = lambda x: bool(re.compile(r'[a-zA-Zа-яА-ЯйЙёЁ_-]').match(x))

    for index in qwery['login']:
        valid = login_pattern(index)

    if qwery['password'] != qwery['repassword']:
        valid = False

    if len(qwery['password']) < 5 and len(qwery['repassword']) < 5:
        valid = False

    if CountUser.objects.filter(login=qwery['login']) or CountUser.objects.filter(email=qwery['email']):
        valid = False

    return valid


def valid_profile(qwery):
    valid = False
    primary_pattern = lambda x: bool(re.compile(r'[a-zA-Zа-яА-ЯйЙёЁ\s-]').match(x))
    bmg_pattern = lambda x: bool(re.compile(r'[a-zA-Zа-яА-ЯйЙёЁ\s0-9-]').match(x))

    for index in qwery['name']:
        valid = primary_pattern(index)
    for index in qwery['surname']:
        valid = primary_pattern(index)
    for index in qwery['country']:
        valid = primary_pattern(index)
    for index in qwery['hobby']:
        valid = primary_pattern(index)
    for index in qwery['like_food']:
        valid = primary_pattern(index)
    for index in qwery['like_music']:
        valid = bmg_pattern(index)
    for index in qwery['like_book']:
        valid = bmg_pattern(index)
    for index in qwery['like_game']:
        valid = bmg_pattern(index)

    return valid
