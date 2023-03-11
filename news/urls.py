from django.urls import path
from .views import NewsList, NewsDetail, CommentDetail, CommentList, LikeDetail, LikeList

app_name = 'news'

urlpatterns = [

    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', NewsDetail.as_view()),
    path('news/<int:pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('news/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('news/<int:pk>/likes', LikeList.as_view(), name='like-list'),
    path('news/likes/<int:pk>', LikeDetail.as_view(), name='like-detail'),

]
