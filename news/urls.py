from django.urls import path
from .views import NewsList, NewsDetail, CommentDetail, CommentList, LikeList

app_name = 'news'

urlpatterns = [

    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', NewsDetail.as_view()),
    path('news/<int:pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('news/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('news/<int:pk>/like', LikeList.as_view(), name='like-list'),

]
