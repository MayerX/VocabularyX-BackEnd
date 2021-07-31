# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Word(models.Model):
    id = models.TextField(blank=True, null=True)
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
