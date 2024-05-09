from rest_framework import serializers
from socials.models import SocialIcons, UserSocials


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialIcons
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True}
        }


class UserSocialsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=UserSocials.objects.all())

    class Meta:
        model = UserSocials
        fields = ['id', 'social_icon', 'links', 'user', 'position']

        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'write_only': True}
        }
