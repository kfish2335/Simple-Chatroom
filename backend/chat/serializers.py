from rest_framework import serializers
from chat.models import chat


class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = '__all__'