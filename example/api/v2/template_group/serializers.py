from rest_framework import serializers

from api.base.serializers import InheritedSerializer


# List
class TemplateGroupListSearchRequestSerializer(InheritedSerializer):
    code = serializers.CharField(
        help_text="`code` of Template Group", allow_null=True, required=False, default=None)
    name = serializers.CharField(
        help_text="`name` of Template Group", allow_null=True, required=False, default=None)
    slug = serializers.CharField(
        help_text="`slug` of Template Group", allow_null=True, required=False, default=None)
    active_flag = serializers.BooleanField(
        help_text="`active_flag` of Template Group", default=True)
    parent_id = serializers.IntegerField(
        help_text="`parent_id` of Template Group", allow_null=True, required=False, default=None)


class TemplateGroupListItemResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")
    code = serializers.CharField(help_text="`code` of Template Group")
    name = serializers.CharField(
        help_text="`name` of Template Group", allow_null=True)
    slug = serializers.CharField(
        help_text="`slug` of Template Group", allow_null=True)
    active_flag = serializers.BooleanField(
        help_text="`active_flag` of Template Group")
    parent_id = serializers.IntegerField(
        help_text="`parent_id` of Template Group", allow_null=True)
    parent_name = serializers.CharField(
        help_text="`parent_name` of Template Group", allow_null=True)


class TemplateGroupListResponseSuccessSerializer(InheritedSerializer):
    item = TemplateGroupListItemResponseSerializer(many=True)
    total_page = serializers.IntegerField(
        help_text="`total_page` of Template Group")
    total_record = serializers.IntegerField(
        help_text="`total_record` of Template Group")
    page = serializers.IntegerField(help_text="`page` of Template Group")


# Detail
class TemplateGroupDetailRequestSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")


class TemplateGroupDetailResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")
    code = serializers.CharField(help_text="`code` of Template Group")
    name = serializers.CharField(
        help_text="`name` of Template Group", allow_null=True)
    slug = serializers.CharField(
        help_text="`slug` of Template Group", allow_null=True)
    active_flag = serializers.BooleanField(
        help_text="`active_flag` of Template Group")
    parent_id = serializers.IntegerField(
        help_text="`parent_id` of Template Group", allow_null=True)


# Create     Update
class TemplateGroupRequestSerializer(InheritedSerializer):
    code = serializers.CharField(
        help_text="`code` of Template Group", allow_null=True, required=True)
    name = serializers.CharField(
        help_text="`name` of Template Group", allow_null=True, required=True)
    slug = serializers.CharField(
        help_text="`slug` of Template Group", allow_null=True, required=True)
    active_flag = serializers.BooleanField(
        help_text="`active_flag` of Template Group", allow_null=False, required=True)
    parent_id = serializers.IntegerField(
        help_text="`parent_id` of Template Group", allow_null=True, required=True)


class TemplateGroupCreateSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")
    created_by = serializers.CharField(
        help_text="`created_by` of Template Group")
    created_at = serializers.DateTimeField(
        help_text="`created_at` of Template Group")


class TemplateGroupUpdateResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")
    updated_by = serializers.CharField(
        help_text="`updated_by` of Template Group")
    updated_at = serializers.DateTimeField(
        help_text="`updated_at` of Template Group")


# Menu
class TemplateGroupMenuRequestSerializer(InheritedSerializer):
    only_parent_menu_flag = serializers.BooleanField(
        help_text="`only_parent_menu_flag`=True khi chỉ cần danh sách Menu Cha", required=False, default=False)


class TemplateGroupListMenuItemResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")
    name = serializers.CharField(help_text="`name` of Template Group")


class TemplateGroupListMenuResponseSuccessSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of Template Group")
    name = serializers.CharField(help_text="`name` of Template Group")
    items = TemplateGroupListMenuItemResponseSuccessSerializer()


class TemplateGroupCheckExistCodeRequestSerializer(InheritedSerializer):
    code = serializers.CharField(help_text="`code` of template group", default=None)
    slug = serializers.CharField(help_text="`slug` of template group", default=None)


class TemplateGroupCheckExistCodeResponseSerializer(InheritedSerializer):
    is_exist = serializers.BooleanField(help_text="`is_exist` of code or slug template group . Nếu true thì đã tồn tại")
