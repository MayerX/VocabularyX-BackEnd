from django.http import JsonResponse
from django.views import View

from .models import Word


# Create your views here.


class word_w_view(View):

    def get(self, request, word_id):
        word = Word.objects.get(id=word_id)

        return JsonResponse(
            data={
                'id': word.id,
                'spell': word.spell,
                'pos': word.pos,
                'cn_etym': word.cn_etym,
                'en_etym': word.en_etym,
                'sentence': word.sentence,
                'phonetic': word.phonetic,
                'word_forms': word.word_forms,
                'audio_sources': word.audio_sources,
                'updated': word.updated,
                'raw': word.raw,
                'parsed': word.parsed
            })


class word_ws_view(View):

    def get(self, request, word_spell):
        word = Word.objects.get(spell=word_spell)

        return JsonResponse(
            data={
                'id': word.id,
                'spell': word.spell,
                'pos': word.pos,
                'cn_etym': word.cn_etym,
                'en_etym': word.en_etym,
                'sentence': word.sentence,
                'phonetic': word.phonetic,
                'word_forms': word.word_forms,
                'audio_sources': word.audio_sources,
                'updated': word.updated,
                'raw': word.raw,
                'parsed': word.parsed
            })
