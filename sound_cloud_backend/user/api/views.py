from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	# def create(self, request, *args, **kwargs):
	# 	serializer = UserSerializer(data = request.data)
	# 	data = {}
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(data, status = 200)
	# 	data = serializer.errors
	# 	return Response(data, status = 400)

	# def perform_create(self, serializer):
	# 	print(self.request.user)
	# 	serializer.save(user = self.request.user)