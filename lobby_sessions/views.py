# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import Session
from .serializers import SessionSerializer
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from rest_framework_jwt.settings import api_settings
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class LobbySessionsViewSet(ModelViewSet):
		queryset = Session.objects.all()
		serializer_class = SessionSerializer
		permission_classes = (AllowAny,)

		def create(self, request): # -TODO = find how to create passing dict/obj/hash
			insider = User.objects.get(username=request.data['insiderUsername'])
			jobSeeker = User.objects.get(username=request.data['jobSeekerUsername'])
			print('INSIDER ==>', insider)
			print('jobSeeker ==>', jobSeeker)
			date = parse_date(request.data['date'])
			title = request.data['title']
			comments = request.data['comments']
			session = Session(id=None, date=date, time='None', insider=insider, jobSeeker=jobSeeker, comments=comments, title=title)
			session.save()

			return JsonResponse({'created': 'created'}, safe=False)

		def list(self, request):
			jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
			user_from_request = jwt_decode_handler(request.META['HTTP_TOKEN'])

			user = User.objects.get(username=user_from_request['username'])
			
			jobSeeker_sessions_query = Session.objects.filter(jobSeeker__username=user.username)
			jobSeeker_sessions = SessionSerializer(jobSeeker_sessions_query, many=True).data

			insider_sessions_query = Session.objects.filter(insider=user.id)
			insider_sessions = SessionSerializer(insider_sessions_query, many=True).data
			
			return JsonResponse({"asJobSeeker": jobSeeker_sessions, "asInsider": insider_sessions}, safe=False)

		def destroy(self, request, *args, **kwargs):
			session = Session.objects.get(pk=request.data['sessionId'])
			session.delete()
			return JsonResponse({"deleted": True}, safe=False)


