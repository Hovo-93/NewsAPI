from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import News, Comment, Like, User


class UserRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('pk',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserRelatedSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'created_at')


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at', 'liked', 'likes', 'comments')

    def get_likes(self, obj):
        return obj.like_set.count()

    def get_liked(self, obj):
        return obj.like_set.filter(user=self.context['request'].user).count() > 0

    def get_comments(self, obj):
        return obj.comment_set.count()
