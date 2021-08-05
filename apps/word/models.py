# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DBForerinkey(models.ForeignKey):
    def db_type(self, connection):
        return 'text'

    def rel_db_type(self, connection):
        return 'text'


class Word(models.Model):
    id = DBForerinkey('WordWordlist', models.CASCADE,
                           primary_key=True, unique=True, to_field='word_id')
    spell = models.TextField(unique=True)
    pos = models.TextField(blank=True, null=True)
    cn_etym = models.TextField(blank=True, null=True)
    en_etym = models.TextField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    phonetic = models.TextField(blank=True, null=True)
    word_forms = models.TextField(blank=True, null=True)
    audio_sources = models.TextField(blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    parsed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'word'


class WordWordlist(models.Model):
    word_id = models.TextField(unique=True)
    wordlist_id = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'word_wordlist'


class Wordlist(models.Model):
    id = DBForerinkey('WordWordlist', models.DO_NOTHING,
                           primary_key=True, unique=True, to_field='wordlist_id')
    name = models.TextField(blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wordlist'
