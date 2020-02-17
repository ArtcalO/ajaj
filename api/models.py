from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
	text = models.TextField()
	def __str__(self):
		return f"{self.user.username} > {self.text[:20]}"

class Comment(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
	text = models.TextField()
	def __str__(self):
		return f"{user.username} > {self.text[:20]}"

