from django.conf.urls import url

from downloader.views import DownloadView, get_progress


urlpatterns = [
    url(r'^download/', DownloadView.as_view(), name='download'),
    url(r'^get_progress/(?P<task_id>[^/]+)/$', get_progress, name='get_progress'),
]
