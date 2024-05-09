from rest_framework import serializers
from theme.models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True}
        }
