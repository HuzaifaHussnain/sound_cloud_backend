from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token


class UserCreateAPIView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = []

	def create(self, request, *args, **kwargs):
		serializer = UserSerializer(data = request.data)
		data = {}
		if serializer.is_valid():
			user = serializer.save()
			if user:
				token = Token.objects.create(user=user)
				data = serializer.data
				data['token'] = token.key
			return Response(data, status=status.HTTP_201_CREATED)
		data = serializer.errors
		return Response(data, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
	def get(self, request, format=None):
		request.user.auth_token.delete()
		return Response(status=status.HTTP_200_OK)

