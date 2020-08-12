from rest_framework import serializers
from song.models import Song, Comment


class CommentSerializer(serializers.ModelSerializer):
	'''
	Serializer class for comments on a Song
	'''
	user = serializers.CharField(source='user.get_username', read_only=True)
	class Meta:
		model = Comment
		fields = ['id', 'body', 'user', 'created_on']

	read_only_fields = ['user']


class SongListSerializer(serializers.ModelSerializer):
	'''
	Serializer class for Song model. It does not serializes comments. 
	'''
	likes_count = serializers.SerializerMethodField()
	liked_by_user = serializers.SerializerMethodField()
	class Meta:
		model = Song
		fields = ['id', 'title', 'views', 'file', 'likes_count', 'liked_by_user']

	def get_likes_count(self, obj):
		return obj.likes.count()

	def get_liked_by_user(self, obj):
		user = self.context['request'].user
		liked = False
		if user in obj.likes.all():
			liked = True
		return liked

class SongSerializer(serializers.ModelSerializer):
	'''
	Serializer class for Song model which includes comments on the song as well.
	'''
	comments = CommentSerializer(many=True, read_only=True)
	likes_count = serializers.SerializerMethodField()
	liked_by_user = serializers.SerializerMethodField()

	class Meta:
		model = Song
		fields = ['id', 'title', 'views', 'file', 'likes_count', 'liked_by_user', 'comments']

	def get_likes_count(self, obj):
		return obj.likes.count()

	def get_liked_by_user(self, obj):
		user = self.context['request'].user
		liked = False
		if user in obj.likes.all():
			liked = True
		return liked

