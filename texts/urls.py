from django.conf.urls import url, include, patterns
from texts.views import hello

urlpatterns = patterns ('',
    url(r'^diarytext/$', diarytext),
)
