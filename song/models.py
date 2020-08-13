from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

class Song(models.Model):
	SONG_FILE_CHOICES = [
		('Audio', 'Audio'),
		('Video','Video'),
	]
	title = models.CharField(max_length=100, null=False, blank=False)
	views = models.IntegerField(default=0)
	tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
	likes = models.ManyToManyField(User, blank=True, related_name='liked_songs')
	media_type = models.CharField(choices=SONG_FILE_CHOICES, max_length=5, default='Audio')
	file = models.FileField(upload_to='songs/', max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return str(self.title)


class Comment(models.Model):
	song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField(null=False, blank=False)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return str(self.body)
