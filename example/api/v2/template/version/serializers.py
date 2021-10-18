from rest_framework import serializers
from api.base.serializers import InheritedSerializer


class VersionResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of template")
    name = serializers.CharField(help_text="`name` of template")
    code = serializers.CharField(help_text="`code` of template")
    version = serializers.FloatField(help_text="`version` of template")
    start_date = serializers.DateTimeField(help_text="`start_date` of template")
    end_date = serializers.DateTimeField(help_text="`end_date` of template")
    updated_by = serializers.CharField(help_text="`updated_by` of template")
