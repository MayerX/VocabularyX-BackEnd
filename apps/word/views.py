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

    def get(self, request):
        response = json.loads(request.body)
        word = Word.objects.get(id=response['id'])
        word_se = WordSerializer(word)
        word_dict = dict(word_se.data)

        for key in keys:
            if word_dict[key] is not None:
                word_dict[key] = demjson.decode(word_dict[key])

        data = {
            "msg": 'succeed',
            "word": word_dict
        }

        return JsonResponse(data=data, status='200')


class wsView(View):

    def get(self, request):
        response = json.loads(request.body)
        word = Word.objects.get(spell=response['spell'])
        word_se = WordSerializer(word)
        word_dict = word_se.data

        for key in keys:
            if word_dict[key] is not None:
                word_dict[key] = demjson.decode(word_dict[key])

        data = {
            "msg": "succeed",
            "word": word_dict,
        }

        return JsonResponse(data=data, status='200')


class sView(View):

    def get(self, request):
        response = json.loads(request.body)
        fragment = response['fragment']
        words = Word.objects.filter(spell__regex="^%s." % fragment)
        words_se = WordSerializer(words, many=True)

        for word in words_se.data:
            for key in keys:
                if word[key] is not None:
                    word[key] = demjson.decode(word[key])

        data = {
            "msg": 'succeed',
            "words": words_se.data,
        }

        return JsonResponse(data=data, status='200')
        # return JsonResponse(words_se.data, safe=False)


class wlsView(View):

    def get(self, request):
        wordlists = Wordlist.objects.all()
        wordlists_se = WordlistSerializer(wordlists, many=True)

        data = {
            "msg": "succeed",
            "wordlists": wordlists_se.data,
        }

        return JsonResponse(data=data, status='200')


class wlView(View):

    def get(self, request):
        response = json.loads(request.body)
        wordlist = Wordlist.objects.get(id=response['id'])
        wordlist_se = WordlistSerializer(wordlist)
        words = wordlist_se.data['word']

        for word in words:
            for key in keys:
                if word[key] is not None:
                    word[key] = demjson.decode(word[key])

        data = {
            "msg": "succeed",
            "wordlist": wordlist_se.data,
        }

        return JsonResponse(data=data, status='200')

    def post(self, request):
        response = json.loads(request.body)

        if 'name' not in response:
            return JsonResponse(data={'msg': 'failure'}, status='400')
        id = str(uuid.uuid4())[-11:-1]
        new_wordlist = Wordlist.objects.create(id=id)
        new_wordlist.name = response['name']
        new_wordlist.word_count = 0
        new_wordlist.save()

        return JsonResponse(
            status=200,
            data={
                'msg': 'succeed'
            }
        )

    def put(self, request):
        response = json.loads(request.body)
        wordlist = Wordlist.objects.get(id=response['id'])
        num = Wordlist.word.all()

        if 'name' in response:
            wordlist.name = response['name']
        wordlist.word_count = num
        wordlist.save()

        return JsonResponse(
            status=200,
            data={
                'msg': 'succeed'
            }
        )

    def delete(self, request):
        response = json.loads(request.body)
        Wordlist.objects.get(id=response['id']).delete()

        return JsonResponse(
            status=200,
            data={
                'msg': 'succeed'
            }
        )


class wordbatchView(View):

    def get(self, request):
        response = json.loads(request.body)
        wordlist = Wordlist.objects.get(id=response['id'])
        words_id = response['words']
        words = list(Word.objects.in_bulk(words_id).values())
        wordlist.word.set(words)

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )

    def put(self, request):
        response = json.loads(request.body)
        wordlist = Wordlist.objects.get(id=response['id'])
        words_id = response['words']
        wordlist.word.clear()
        words = list(Word.objects.in_bulk(words_id).values())
        wordlist.word.set(words)

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )

    def delete(self, request):
        response = json.loads(request.body)
        wordlist = Wordlist.objects.get(id=response['id'])
        words_id = response['words']
        words = list(Word.objects.in_bulk(words_id).values())
        wordlist.word.remove(*words)

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )