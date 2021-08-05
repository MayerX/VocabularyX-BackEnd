from rest_framework import serializers
import demjson


class WordSerializer(serializers.Serializer):
    id = serializers.CharField()
    spell = serializers.CharField()
    pos = serializers.CharField()
    cn_etym = serializers.CharField()
    en_etym = serializers.CharField()
    sentence = serializers.CharField()
    phonetic = serializers.CharField()
    word_forms = serializers.CharField()
    audio_sources = serializers.CharField()
    updated = serializers.IntegerField()
    raw = serializers.CharField()
    parsed = serializers.IntegerField()
