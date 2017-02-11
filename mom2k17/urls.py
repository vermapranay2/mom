from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    # url(r'^subscribe/$', views.subscribeView, name='subscribe'),
    url(r'^about$', views.about, name='about'),
    url(r'^events$', views.events, name='events'),
    url(r'^appcorner$', views.appcorner, name='appcorner'),
    url(r'^brainwave$', views.brainwave, name='brainwave'),
    url(r'^expressions$', views.expressions, name='expressions'),
    url(r'^flash$', views.flash, name='flash'),
    url(r'^hospi$', views.hospi, name='hospi'),
    url(r'^osd$', views.osd, name='osd'),
    url(r'^quiz$', views.quiz, name='quiz'),
    url(r'^sponsors$', views.sponsors, name='sponsors'),
    url(r'^team$', views.team, name='team'),
    url(r'^tme$', views.tme, name='tme'),
    url(r'^message', views.message, name='message'),
    url(r'^workshop', views.workshop, name='workshop'),
    # url(r'^register$', views.register, name='register'),
    url(r'^register$', views.register.as_view(), name='register'),


    ]