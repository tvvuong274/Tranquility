from rest_framework import serializers

from api.base.serializers import InheritedSerializer
from idm_config.settings import DATETIME_INPUT_OUTPUT_FORMAT


class UserLoginSuccessResponseSerializer(InheritedSerializer):
    user_id = serializers.IntegerField(help_text="`id` of user")
    name = serializers.CharField(help_text="`name` of user")
    token = serializers.CharField(help_text="Bearer token")


class UserCreateSuccessResponseSerializer(InheritedSerializer):
    user_id = serializers.IntegerField(help_text="`id` of user")
    name = serializers.CharField(help_text="`name` of user")


class UserCreateRequestSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` of user")
    username = serializers.CharField(help_text="`username` of user")
    password = serializers.CharField(help_text="`password` of user")


class UserUpdateRequestSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` of user")


class UserDetailSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of user")
    name = serializers.CharField(help_text="`name` of user")
    created_at = serializers.DateTimeField(help_text=f"`created_at`, must have the format `{DATETIME_INPUT_OUTPUT_FORMAT}`")
    updated_at = serializers.DateTimeField(help_text=f"`updated_at`, must have the format `{DATETIME_INPUT_OUTPUT_FORMAT}`")


class UserListSuccessResponeSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` Name of User")
    username = serializers.CharField(help_text="`user_name` User Name  of User")
    id = serializers.IntegerField(help_text="`id` User Id  of User")