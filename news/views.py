import datetime

from django.shortcuts import render, redirect
from rest_framework.response import Response
from pytz import utc
from rest_framework import viewsets, generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import News, User, UserRoles, Comment, Like
from .permissions import IsOwnerOrReadOnly, IsAdminRole, IsNewsAuthor

from .serializers import NewsSerializer, CommentSerializer, LikeSerializer
from .paginations import NewsListPagination


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
        news_item = News.objects.get(id=self.kwargs['id'])
        serializer.save(user=self.request.user, news=news_item)

    def get_queryset(self):
        news_item = News.objects.get(id=self.kwargs['id'])
        return Comment.objects.filter(news=news_item)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminRole, IsNewsAuthor]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # get)object() returns the object instance if it nor http404 exep
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        news_item = News.objects.get(id=self.kwargs['id'])
        serializer.save(user=self.request.user, news=news_item)

    def get_queryset(self):
        news_item = News.objects.get(id=self.kwargs['id'])
        return Like.objects.filter(news=news_item)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]
