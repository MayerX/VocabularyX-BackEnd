from django.db import models

from apps.word import models as word_model


# Create your models here.

class Section(models.Model):
    id = models.TextField(primary_key=True, unique=True)
    duration = models.IntegerField()
    index = models.IntegerField()
    words = models.ManyToManyField(word_model.Word, through='WordSection')

    class Meta:
        db_table = 'section'


class Plan(models.Model):
    id = models.TextField(primary_key=True, unique=True)
    name = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    duration = models.IntegerField()
    sections = models.ForeignKey(Section, models.CASCADE)

    class Meta:
        db_table = 'plan'


class WordSection(models.Model):
    word_id = models.ForeignKey(word_model.Word, models.CASCADE, unique=True)
    section_id = models.ForeignKey(Section, models.DO_NOTHING, unique=True)

    class Meta:
        db_table = 'word_section'
