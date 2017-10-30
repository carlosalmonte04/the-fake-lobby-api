from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, validated_data):
    	user = UserSerializer(validated_data.data)
    	user = User.objects.create_user(user.data['username'], None, user.data['password'])
    	if user is not None:
    		payload = jwt_payload_handler(user)
    		token = jwt_encode_handler(payload)
    		return JsonResponse({'token': token})
    	else:
    		return JsonResponse({'error': 'user could not be created'})

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer