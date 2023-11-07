import re


def valid_register(qwery):
    valid = True
    login = lambda x: bool(re.compile(r'[a-zA-Zа-яА-ЯйЙёЁ_-]').match(x))

    for index in qwery['login']:
        valid = login(index)

    if qwery['password'] != qwery['repassword']:
        valid = False

    if len(qwery['password']) < 7 and len(qwery['repassword']) < 7:
        valid = False

    return valid
