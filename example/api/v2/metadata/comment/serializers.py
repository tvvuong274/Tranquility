from rest_framework import serializers
from api.base.serializers import InheritedSerializer


class MetadataCommentCreateUpdateRequestSerializer(InheritedSerializer):
    content = serializers.CharField(help_text="`content` Comment of user (HMTL)", allow_null=False, required=True)


class MetadataCommentCreateResponeSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` Metadata-Comment Id created")
    created_by = serializers.CharField(help_text="`create_by` User name who created Metadata-Comment")


class MetadataCommentUpdateResponeSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` Metadata-Comment Id created")
    updated_by = serializers.CharField(help_text="`create_by` User name who created Metadata-Comment")


class MetadataCommentResponseListSerializer(InheritedSerializer):
    userid = serializers.IntegerField(help_text="`user_id` User-Id")
    username = serializers.CharField(help_text="`user_name` User-Name")
    name = serializers.CharField(help_text="`name` Name of User")
    avatar_url = serializers.CharField(help_text="`avatar_url` Avatar Url of User")
    content = serializers.CharField(help_text="`content` Content of MetadataComment")
    log_flag = serializers.BooleanField(help_text="`content` Content of MetadataComment")
    created_at = serializers.DateTimeField(help_text="`created_at` DateTime created")
    updated_at = serializers.DateTimeField(help_text="`updated_at` DateTime updated")
