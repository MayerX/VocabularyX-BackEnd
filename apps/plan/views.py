import json
import uuid

import demjson
from django.http import JsonResponse
# Create your views here.
from django.views import View

from apps.word.models import Word
from .models import Plan, Section
from .serializer import PlanSerializer, SectionSerializer

keys = ['pos', 'phonetic', 'word_forms', 'audio_sources']


class plansView(View):

    def get(self, request):
        plans = Plan.objects.all()
        plans_se = PlanSerializer(plans, many=True)

        data = {
            'msg': 'succeed',
            'plans': plans_se.data
        }

        return JsonResponse(data=data, status='200')


class planView(View):

    def get(self, request):
        response = json.loads(request.body)

        if 'id' in response:
            id = response['id']
            plan = Plan.objects.get(id=id)
            plan_se = PlanSerializer(plan)

            data = {
                'msg': 'succeed',
                'plan': plan_se.data,
            }

            return JsonResponse(data=data, status='200')
        return JsonResponse(data={'msg': 'failure'}, status='400')

    def post(self, request):
        response = json.loads(request.body)
        id = str(uuid.uuid4())[-11:-1]

        new_plan = Plan.objects.create(id=id)
        new_plan.name = response['name']
        new_plan.start_time = response['start_time']
        new_plan.end_time = response['end_time']
        new_plan.word_num = response['word_num']
        new_plan.duration = 0
        new_plan.save()

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )

    def put(self, request):
        response = json.loads(request.body)
        plan = Plan.objects.get(id=response['id'])

        if 'name' in response:
            plan.name = response['name']
        if 'start_time' in response:
            plan.start_time = response['start_time']
        if 'end_time' in response:
            plan.end_time = response['end_time']
        if 'duration' in response:
            plan.duration = response['duration']
        if 'word_num' in response:
            plan.word_num = response['word_num']
        plan.save()

        return JsonResponse(data={'msg': 'succeed'}, status='200')

    def delete(self, request):
        response = json.loads(request.body)
        Plan.objects.get(id=response['id']).delete()

        return JsonResponse(data={'msg': 'succeed'}, status='200')


class secView(View):

    def get(self, request):
        response = json.loads(request.body)

        section = Section.objects.get(id=response['id'])
        section_se = SectionSerializer(section)
        words = section_se.data['words']

        for word in words:
            for key in keys:
                if word[key] is not None:
                    word[key] = demjson.decode(word[key])

        data = {
            'msg': 'succeed',
            'section': section_se.data
        }

        return JsonResponse(data=data, status='200')

    def post(self, request):
        response = json.loads(request.body)
        id = str(uuid.uuid4())[-11:-1]

        plan = Plan.objects.get(id=response['plan_id'])
        new_section = Section.objects.create(id=id)
        new_section.duration = 0
        new_section.plan = plan
        new_section.index = len(plan.section_set.all()) + 1
        new_section.save()

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )

    def put(self, request):
        response = json.loads(request.body)
        section = Section.objects.get(id=response['id'])

        if 'index' in response:
            max_index = len(section.plan.section_set.all())
            update = response['index']
            if int(update) > max_index:
                return JsonResponse(
                    status='400',
                    data={
                        'msg': 'failure'
                    }
                )
            else:
                primary_scetion = Section.objects.get(plan=section.plan, index=update)
                primary_scetion.index = section.index
                section.index = update
                primary_scetion.save()
        if 'duration' in response:
            section.duration = response['duration']
        section.save()

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )

    def delete(self, request):
        response = json.loads(request.body)
        Section.objects.get(id=response['id']).delete()

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )


class secaddView(View):

    def get(self, request):
        response = json.loads(request.body)
        section = Section.objects.get(id=response['id'])
        word = Word.objects.get(id=response['id'])
        section.words.add(word)

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )


class secdelView(View):

    def get(self, request):
        response = json.loads(request.body)
        section = Section.objects.get(id=response['id'])
        word = Word.objects.get(id=response['id'])
        section.words.remove(word)

        return JsonResponse(
            status='200',
            data={
                'msg': 'succeed'
            }
        )
