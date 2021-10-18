from rest_framework import serializers
from api.base.serializers import InheritedSerializer


class BlockListResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of block")
    name = serializers.CharField(help_text="`name` of block")


class DepartmentListResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of department")
    name = serializers.CharField(help_text="`name` of department")
