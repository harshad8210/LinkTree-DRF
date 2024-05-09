from rest_framework import serializers
from links.models import Link, UserLink


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True}
        }


class UserLinkSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=UserLink.objects.all())

    class Meta:
        model = UserLink
        fields = ['id', 'link_key', 'title', 'links', 'position', 'thumbnail_url', 'user']

        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'write_only': True}
        }
