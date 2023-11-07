from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CountUser(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repassword = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {} - {}'.format(self.login, self.password, self.email)


class StatusUser(models.Model):
    SEX_CHOICES = (('Male', 'Male'), ('Female', 'Female'))

    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.DateField('Age')
    sex = models.CharField('Sex', max_length=10, choices=SEX_CHOICES, default='Male')
    country = models.CharField('Country', max_length=50)
    hobby = models.CharField('Hobby', max_length=50)
    like_food = models.CharField('Like food', max_length=50)
    like_music = models.CharField('Like music', max_length=50)
    like_book = models.CharField('Like book', max_length=50)
    like_game = models.CharField('Like game', max_length=50)
    slug = models.SlugField('Slug', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.surname, self.age)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('{}-{}-{}-{}-{}'.format(self.name, self.surname, self.age, self.sex, self.country))
        super(StatusUser, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('about_page', kwargs={'user_slug': self.slug})
