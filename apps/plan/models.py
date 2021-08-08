from django.db import models

from apps.word import models as word_model


# Create your models here.


class Plan(models.Model):
    id = models.TextField(primary_key=True, unique=True)
    name = models.TextField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    word_num = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'plan'


class WordSection(models.Model):
    word_id = models.ForeignKey(word_model.Word, models.CASCADE)
    section_id = models.ForeignKey('Section', models.DO_NOTHING)

    class Meta:
        db_table = 'word_section'


class Section(models.Model):
    id = models.TextField(primary_key=True, unique=True)
    duration = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    words = models.ManyToManyField(word_model.Word, through='WordSection')
    plan = models.ForeignKey(Plan, models.CASCADE, blank=True, null=True, to_field='id')

    class Meta:
        db_table = 'section'
