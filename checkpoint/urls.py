from django.conf.urls import url

from . import views

app_name = 'checkpoint'
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    #url(r'^input/$', views.input_view, name='input'),
    #url(r'^thanks/$', views.thanks_view, name='thanks'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
