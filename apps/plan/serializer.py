from rest_framework import serializers

from apps.word.serializer import WordSerializer


class PlanSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    start_time = serializers.DateField()
    end_time = serializers.DateField()
    duration = serializers.IntegerField()


class SectionSerializer(serializers.Serializer):
    id = serializers.CharField()
    index = serializers.IntegerField()
    duration = serializers.IntegerField()
    plan = PlanSerializer(read_only=True)
    words = WordSerializer(read_only=True, many=True)