from rest_framework import serializers
from login.models import User
from links.serializer import UserLinkSerializer
from socials.serializer import UserSocialsSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'is_verified', 'social_link_position', 'theme_key']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    link_user = UserLinkSerializer(many=True)
    social_user = UserSocialsSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_verified', 'social_link_position', 'theme_key',
                  'link_user', 'social_user']


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)


class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
