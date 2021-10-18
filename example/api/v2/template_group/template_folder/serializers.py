from rest_framework import serializers
from api.base.serializers import InheritedSerializer


class FolderCreateRequestSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` of folder", allow_null=False, required=True)
    slug = serializers.CharField(help_text="`slug` of folder", allow_null=False, required=True)
    parent_id = serializers.IntegerField(help_text="`parent_id` of folder", allow_null=True, required=True)


class FolderCreateSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id update` of folder")
    name = serializers.CharField(help_text="`name` of folder")
    created_by = serializers.CharField(help_text="`created_by` of folder")


class FolderUpdateRequestSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` of folder", allow_null=False, required=True)
    slug = serializers.CharField(help_text="`slug` of folder", allow_null=False, required=True)


class FolderUpdateSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id update` of folder")
    created_by = serializers.CharField(help_text="`created_by` of folder")
    updated_by = serializers.CharField(help_text="`updated_by` of folder")


class TemplateFolderListChildResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template folder")
    slug = serializers.CharField(help_text="`slug` of folder")
    name = serializers.CharField(help_text="`name` of folder")
    updated_by = serializers.CharField(help_text="`updated_by` of folder")
    updated_at = serializers.CharField(help_text="`updated_at` of folder")


class TemplateFolderListResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template folder")
    slug = serializers.CharField(help_text="`slug` of folder")
    name = serializers.CharField(help_text="`name` of folder")
    updated_by = serializers.CharField(help_text="`updated_by` of folder")
    updated_at = serializers.CharField(help_text="`updated_at` of folder")
    child = TemplateFolderListChildResponseSuccessSerializer(many=True)


class TemplateFolderMenuRequestSerializer(InheritedSerializer):
    parent_id = serializers.IntegerField(help_text="`parent_id` of template_folder", default=None)


class TemplateFolderListMenuChildResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template folder")
    name = serializers.CharField(help_text="`name` of folder")


class TemplateFolderListMenuResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template folder")
    name = serializers.CharField(help_text="`name` of folder")
    child = TemplateFolderListMenuChildResponseSuccessSerializer(many=True)


class TemplateFolderCheckExistSlugRequestSerializer(InheritedSerializer):
    slug = serializers.CharField(help_text="`slug` of template folder")


class TemplateFolderCheckExistSlugResponseSerializer(InheritedSerializer):
    is_exist = serializers.BooleanField(
        help_text="`is_exist` of slug in template folder . Nếu true thì slug đã tồn tại"
    )
