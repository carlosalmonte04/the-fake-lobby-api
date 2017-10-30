# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import Session
from .serializers import SessionSerializer
from django.contrib.auth.models import User

# Create your views here.

class LobbySessionsViewSet(ModelViewSet):
		queryset = Session.objects.all()
		serializer_class = SessionSerializer
		permission_classes = (AllowAny,)

		def create(self, validated_data):
			print("WHAAAT DIDNT GET HERE!!")
			session = SessionSerializer(validated_data.data)
			insider = User.objects.get(username=validated_data.data['insider'])
			jobSeeker = User.objects.get(username=validated_data.data['jobSeeker'])
			# Session.create()
			# user = User.objects.create_user(user.data['username'], None, user.data['password'])
			return JsonResponse({'created': 'created'}, safe=False)