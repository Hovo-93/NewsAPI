import datetime

from django.shortcuts import render, redirect
from pytz import utc
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from .models import News, Comment, Like, UserRoles
from .paginations import NewsListPagination
from .permissions import IsOwnerOrReadOnly, IsAdminRole, IsNewsAuthor, IsLikedNews
from .serializers import NewsSerializer, CommentSerializer, LikeSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = NewsListPagination


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance.author)
        # if instance.author != self.request.user:
        if not (IsOwnerOrReadOnly or IsAdminRole):
            raise PermissionDenied("You do not have permission to perform this action.")

        instance.created_at = datetime.datetime.utcnow().replace(tzinfo=utc)
        instance.save()


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        news_item = News.objects.get(id=self.kwargs['pk'])
        serializer.save(user=self.request.user, news=news_item)

    def get_queryset(self):
        news_item = News.objects.get(id=self.kwargs['pk'])
        return Comment.objects.filter(news=news_item)


class CommentDetail(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all() # todo nahooy nado ?
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminRole | IsNewsAuthor]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # get)object() returns the object instance if it nor http404 exep
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# todo rename
class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsLikedNews]

    def perform_create(self, serializer):
        print('aaa')
        news_item = News.objects.get(id=self.kwargs['pk'])
        serializer.save(user=self.request.user, news=news_item)
