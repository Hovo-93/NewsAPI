from rest_framework import serializers
from .models import News, Comment, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'news')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username', read_only=True)
    # news = serializers.StringRelatedField(source='news.title')#todo

    class Meta:
        model = Comment
        fields = ('id', 'user', 'news', 'text', 'created_at')


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at', 'likes', 'comments')

    def get_likes(self, obj):
        return obj.like_set.count()  # like_set ete related name chenq greum djanfon default dnum e

    def get_comments(self,obj):
        return  obj.comment_set.count()