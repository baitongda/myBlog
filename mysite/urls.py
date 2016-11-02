#coding=utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

# from . import blog.views
from blog.views import index,hello,main,blog1,index2,ajax_dict,ajax_time,search_id

# url用正则表达式
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^index2/$', index2),
    url(r'^hello/$', hello),
    url(r'^main/', main),
    url(r'^index2/blog/blog1', blog1),
    url(r'^index/ajax_dict/$', ajax_dict),
    url(r'^index/ajax_time/$', ajax_time),

    url(r'^blog/(?P<id>\d+)/$', search_id, name='page')
]
