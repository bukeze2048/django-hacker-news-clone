from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('by/<str:username>/', views.by_author, name='by_author'),
    path('search/', views.search, name='search'),
    path('submit/', views.submit, name='submit'),
    path('<int:news_item_id>/comments/', views.comments, name='comments'),
    path('<int:news_item_id>/comments/<int:comment_id>/reply', views.reply, name='reply'),
]
