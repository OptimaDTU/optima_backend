from django.conf.urls import url
from modules.api import views

urlpatterns = (
    url(r'^$', views.ModuleListView.as_view()),
    url(r'^(?P<slug>[-\w]+)/$', views.ModuleDetailView.as_view()),
    url(r'^(?P<module_slug>[-\w]+)/(?P<video_slug>[-\w]+)/$', views.VideoDetailView.as_view()),
)
