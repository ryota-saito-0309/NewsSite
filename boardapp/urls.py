from django.urls import path, include
from .views import NewsList, NewsDetail, goodfunc, readfunc

urlpatterns = [
    path('', NewsList.as_view(), name='list'),
    path('list2/', NewsList.as_view(), name='list'),
    path('detail/<int:pk>', NewsDetail.as_view(), name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),

]
