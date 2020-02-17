from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = "__all__"

	def create(self, validated_data):
		validated_data['user'] = self.context['request'].user
		print(validated_data['user'])
		obj = Post(user=self.context['request'].user, text=validated_data['text'])
		obj.save()
		return obj

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = "__all__"
		# depth = 1

	def create(self, validated_data):
		validated_data['user'] = self.context['request'].user
		obj = Comment(user=self.context['request'].user,
			post = validated_data['post'], text=validated_data['text'])
		obj.save()
		return obj