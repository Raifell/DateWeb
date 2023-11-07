import datetime
from meeter.models import *


def commit_login(qwery):
    CountUser.objects.create(login=qwery['login'],
                             password=qwery['password'],
                             repassword=qwery['repassword'],
                             email=qwery['email'])


def commit_profile(qwery):
    StatusUser.objects.create(name=qwery['name'],
                              surname=qwery['surname'],
                              age=datetime.datetime.strptime(qwery['age'], '%Y-%m-%d').date(),
                              sex=qwery['sex'],
                              country=qwery['country'],
                              hobby=qwery['hobby'],
                              like_food=qwery['like_food'],
                              like_music=qwery['like_music'],
                              like_book=qwery['like_book'],
                              like_game=qwery['like_game'])
