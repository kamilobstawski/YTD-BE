from rest_framework import serializers


class DownloadSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255)
