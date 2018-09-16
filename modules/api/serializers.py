from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Profile
from modules.models import Module, Tag, Resource, Video


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')


class CuratorSerializer(serializers.ModelSerializer):
    user = AuthUserSerializer()

    class Meta:
        model = Profile
        fields = ('user',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class VideoListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    creator = CuratorSerializer()

    class Meta:
        model = Video
        exclude = ('next_video',)


class ModuleDetailSerializer(serializers.ModelSerializer):
    videos = VideoListSerializer(many=True, read_only=True)
    curators = CuratorSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = '__all__'


class ModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        exclude = ('curators',)


class VideoDetailSerializer(serializers.ModelSerializer):
    module = ModuleListSerializer()
    tags = TagSerializer(many=True, read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)
    creator = CuratorSerializer()
    next_video_slug = serializers.SerializerMethodField()
    previous_video_slug = serializers.SerializerMethodField()

    class Meta:
        model = Video
        exclude = ('next_video',)

    @staticmethod
    def get_previous_video_slug(obj):
        try:
            return obj.previous_video.slug
        except Video.DoesNotExist:
            return None

    @staticmethod
    def get_next_video_slug(obj):
        if obj.next_video:
            return obj.next_video.slug
        else:
            return None
