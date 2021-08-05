import json

import demjson
from django.http import JsonResponse
from django.views import View

from .models import Word
from .serializer import WordSerializer

# Create your views here.

keys = ['pos', 'phonetic', 'word_forms', 'audio_sources']


class wView(View):

    def get(self, request, word_id):
        word = Word.objects.get(id=word_id)
        word_se = WordSerializer(word)

        word_dict = dict(word_se.data)

        for key in keys:
            word_dict[key] = demjson.decode(word_dict[key])

        return JsonResponse(word_dict, safe=False)


class wsView(View):

    def get(self, request, word_spell):
        word = Word.objects.get(spell=word_spell)
        word_se = WordSerializer(word)

        word_dict = dict(word_se.data)

        for key in keys:
            word_dict[key] = demjson.decode(word_dict[key])

        return JsonResponse(word_dict, safe=False)


class sView(View):

    def get(self, request, fragment):
        words = Word.objects.filter(spell__regex="^%s." % fragment)
        words_se = WordSerializer(words, many=True)

        for word in words_se.data:
            for key in keys:
                if word[key] is not None:
                    word[key] = demjson.decode(word[key])

        return JsonResponse(words_se.data, safe=False)