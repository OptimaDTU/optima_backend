from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404

from modules.api.serializers import ModuleListSerializer, ModuleDetailSerializer, VideoDetailSerializer
from modules.models import Module, Video


class ModuleListView(ListAPIView):
    serializer_class = ModuleListSerializer
    queryset = Module.objects.all()

    def get_queryset(self):
        if self.request.GET.get('tags'):
            tags = self.request.GET['tags'].split(',')
            return Module.objects.filter(videos__tags__slug__in=tags)
        return Module.objects.all()

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super(ModuleListView, self).dispatch(*args, **kwargs)


class ModuleDetailView(RetrieveAPIView):
    serializer_class = ModuleDetailSerializer

    def get_object(self):
        return get_object_or_404(Module, slug=self.kwargs['slug'])

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super(ModuleDetailView, self).dispatch(*args, **kwargs)


class VideoDetailView(RetrieveAPIView):
    serializer_class = VideoDetailSerializer

    def get_object(self):
        return get_object_or_404(Video, slug=self.kwargs['video_slug'], module__slug=self.kwargs['module_slug'])

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super(VideoDetailView, self).dispatch(*args, **kwargs)