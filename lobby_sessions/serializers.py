from rest_framework.serializers import ModelSerializer

from models import Session

class SessionSerializer(ModelSerializer):
	class Meta:
		model = Session
		fields = ('insider', 'jobSeeker', 'date', 'title', 'comments', 'time')