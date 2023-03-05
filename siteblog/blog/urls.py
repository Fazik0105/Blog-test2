from django.urls import path

from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('', Home.as_view(), name='home'),
    # path('category/<str:slug>/', get_category, name='category'),
    path('category/<str:slug>/', PostByCategoy.as_view(), name='category'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]
