import json
import uuid

import demjson
from django.http import JsonResponse
from django.views import View

from .models import Word, Wordlist
from .serializer import WordSerializer, WordlistSerializer

# Create your views here.

keys = ['pos', 'phonetic', 'word_forms', 'audio_sources']


class wView(View):

    def get(self, request, word_id):
        word = Word.objects.get(id=word_id)
        word_se = WordSerializer(word)

        word_dict = dict(word_se.data)

        for key in keys:
            if word_dict[key] is not None:
                word_dict[key] = demjson.decode(word_dict[key])

        data = {
            "word": word_dict,
            "msg": 'succeed'
        }

        return JsonResponse(data=data)


class wsView(View):

    def get(self, request, word_spell):
        word = Word.objects.get(spell=word_spell)
        word_se = WordSerializer(word)
        word_dict = dict(word_se.data)

        for key in keys:
            if word_dict[key] is not None:
                word_dict[key] = demjson.decode(word_dict[key])

        data = {
            "word": word_dict,
            "msg": "succeed"
        }

        return JsonResponse(data=data)


class sView(View):

    def get(self, request, fragment):
        words = Word.objects.filter(spell__regex="^%s." % fragment)
        words_se = WordSerializer(words, many=True)

        for word in words_se.data:
            for key in keys:
                if word[key] is not None:
                    word[key] = demjson.decode(word[key])

        data = {
            "words": words_se.data,
            "msg": 'succeed'
        }

        return JsonResponse(data=data)
        # return JsonResponse(words_se.data, safe=False)


class wlsView(View):

    def get(self, request):
        wordlists = Wordlist.objects.all()
        wordlists_se = WordlistSerializer(wordlists, many=True)

        data = {
            "wordlists": wordlists_se.data,
            "msg": "succeed"
        }

        return JsonResponse(data=data, safe=False)


class wlView(View):

    def get(self, request):
        id = request.GET['id']
        wordlist = Wordlist.objects.get(id=id)
        wordlist_se = WordlistSerializer(wordlist)
        words = wordlist_se.data['word']

        for word in words:
            for key in keys:
                if word[key] is not None:
                    word[key] = demjson.decode(word[key])

        data = {
            "wordlist": wordlist_se.data,
            "msg": "succeed"
        }

        return JsonResponse(data=data, status='200')

    def post(self, request):
        name = request.POST['name']
        id = str(uuid.uuid4())[-11:-1]
        new_wordlist = Wordlist.objects.create(id=id)
        new_wordlist.name = name
        new_wordlist.word_count = 0
        new_wordlist.save()

        return JsonResponse(
            status=200,
            data={
                'msg': 'succeed'
            }
        )

    def put(self, request):
        id = request.GET['id']
        wordlist = Wordlist.objects.get(id=id)
        num = Wordlist.word.all()

        parms = str(request.body, 'utf-8').split('&')
        for parm in parms:
            parm = parm.split('=')
            if parm[0] == 'name':
                wordlist.name = parm[1]
        wordlist.word_count = num
        wordlist.save()

        return JsonResponse(
            status=200,
            data={
                'msg': 'succeed'
            }
        )

    def delete(self, request):
        id = request.GET['id']
        Wordlist.objects.get(id=id).delete()

        return JsonResponse(
            status=200,
            data={
                'msg': 'succeed'
            }
        )


class waddView(View):

    def get(self, request, word_id, wordlist_id):
        wordlist = Wordlist.objects.get(id=wordlist_id)
        word = Word.objects.get(id=word_id)
        wordlist.word.add(word)

        return JsonResponse(
            data={
                "msg": "succeed",
            },
            status='200'
        )


class wdelView(View):

    def get(self, request, word_id, wordlist_id):
        wordlist = Wordlist.objects.get(id=wordlist_id)
        word = Word.objects.get(id=word_id)
        wordlist.word.remove(word)

        return JsonResponse(
            data={
                "msg": "succeed"
            },
            status='200',
        )
