from rest_framework import serializers


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


class WordlistSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    create_time = serializers.DateField()
    update_time = serializers.DateField()
    word_count = serializers.IntegerField()
    word = WordSerializer(many=True, read_only=True)
