from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r"^(?P<blog_id>\d+)/$", views.detail, name='detail'),
    url(r"^(?P<blog_id>\d+)/delete/$", views.delete, name='delete'),
    url(r"^(?P<blog_id>\d+)/update/$", views.update, name='update'),
    url(r"^new/$", views.create, name='create'),
    url(r"^(?P<tag>\w+)/$", views.tag_filter, name='tag_filter'),
    )
