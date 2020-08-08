from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
	''' Serializer class for User model '''
	email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		''' Overriding the default create function for UserSerializer '''
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		return user
