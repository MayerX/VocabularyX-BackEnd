from rest_framework import serializers


class WordSerializer(serializers.Serializer):
    id = serializers.CharField()
    spell = serializers.CharField()
    pos = serializers.CharField()
