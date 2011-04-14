#coding: utf-8

#######################################
# TESTING PURPOSE ONLY MODELS!!       #
# DO NOT ADD THE APP TO INSTALLED_APPS#
#######################################

from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

GENDER_CH = [('M', 'male'), ('F', 'female')]

class Person(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CH)
    happy = models.BooleanField(default=True)
    name = models.CharField(max_length=30)
    nickname = models.SlugField(null=True)
    age = models.IntegerField()
    bio = models.TextField(null=True)
    birthday = models.DateField()
    appointment = models.DateTimeField()
    blog = models.URLField()

    #backward compatibilty with Django 1.1
    try:
        wanted_games_qtd = models.BigIntegerField()
    except AttributeError:
        wanted_games_qtd = models.IntegerField()

class Dog(models.Model):
    owner = models.ForeignKey('Person')
    breed = models.CharField(max_length=50)

class Store(models.Model):
    customers = models.ManyToManyField(Person, related_name='favorite_stores', blank=True, null=True)
    employees = models.ManyToManyField(Person, related_name='employers')

class DummyIntModel(models.Model):
    int_field = models.IntegerField()
    small_int_field = models.SmallIntegerField()
    try:
        big_int_field = models.BigIntegerField()
    except AttributeError:
        big_int_field = models.IntegerField()


class DummyPositiveIntModel(models.Model):
    positive_small_int_field = models.PositiveSmallIntegerField()
    positive_int_field = models.PositiveIntegerField()

class DummyNumbersModel(models.Model):
    float_field = models.FloatField()

class DummyDecimalModel(models.Model):
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)

class UnsupportedField(models.Field):
    description = "I'm bad company, mommy doesn't know me"
    def __init__(self, *args, **kwargs):
        super(UnsupportedField, self).__init__(*args, **kwargs)

class UnsupportedModel(models.Model):
    unsupported_field = UnsupportedField()

class DummyEmailModel(models.Model):
    email_field = models.EmailField()

class ModelWithSelfReference(models.Model):
    self_reference = models.ForeignKey('self', null=True)

class DummyGenericForeignKeyModel(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

class DummyGenericRelationModel(models.Model):
    relation = generic.GenericRelation(DummyGenericForeignKeyModel)