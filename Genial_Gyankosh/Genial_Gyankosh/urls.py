"""Genial_Gyankosh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from Gyankosh_UI.views import *

import Gyankosh_API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Gyankosh/',include('Gyankosh_API.urls')),
    url(r'^$', login, name='login'),
    url(r'logout$', logout, name='logout'),
    url(r'dashboard$', dashboard, name='dashboard'),
    url(r'question$', question, name='question'),
    url(r'questions$', questions, name='questions'),
    # url(r'answer$', answer, name='answer'),
    url(r'ins_answer$', ins_answer, name='ins_answer'),
    # url(r'answer$', answer, name='answer'),
    url(r'question/(?P<problem_id>\d+)/$', answerbyid, name='question'),
    # url(r'question/(?P<xx.ProblemID>[\w\-]+)//$', answerbyid, name='question'),
    url(r'answer/(?P<solution_id>\d+)/(?P<problem_id>\d+)/$', verifyans, name='verifyans'),

    path('load-controller/', load_control, name='ajax_load_controller'),
    path('load-question/', load_que, name='ajax_load_question'),


]

urlpatterns += staticfiles_urlpatterns()
