from library.constant.metadata import METADATA_SYSTEM_TYPE_LIST
from library.constant.template import (
    TEMPLATE_DEFAULT_SORT_A_TO_Z, 
)
from rest_framework import serializers
from api.base.serializers import InheritedSerializer


# List
class TemplateSearchSerializer(InheritedSerializer):
    # Request
    template_folder_id = serializers.IntegerField(
        help_text="`template_folder_id` of Template Folder")

    # Search
    name = serializers.CharField(
        help_text="`name` of template, Tìm kiếm theo Tên biểu mẫu", 
        allow_null=True, 
        required=False, 
        default=None
    )
    sort = serializers.IntegerField(
        help_text="`sort` of template, Sắp xếp: Mặc định A-Z", default=TEMPLATE_DEFAULT_SORT_A_TO_Z)
    start_date = serializers.DateField(
        help_text="`start_date` of template, Ngày hiệu lực: Mặc định `chưa rõ`",
        allow_null=True,
        required=False)
    end_date = serializers.DateField(
        help_text="`end_date` of template, Ngày hết hiệu lực: Mặc định `chưa rõ`",
        allow_null=True,
        required=False)


class TemplateListItemSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of template")
    name = serializers.CharField(
        help_text="`name` of template, Tên văn bản", allow_null=True)
    version = serializers.FloatField(
        help_text="`version` of template, Phiên bản", allow_null=False)
    start_date = serializers.DateField(
        help_text="`start_date` of template, Ngày hiệu lực")
    updated_by = serializers.CharField(
        help_text="`updated_by` of template, Người cập nhật gần nhất")
    updated_at = serializers.DateTimeField(
        help_text="`updated_at` of template, Thời gian cập nhật gần nhất")
    c_status = serializers.BooleanField(
        help_text="`c_status` of template, Trạng thái hoạt động")
    list_system_type_name = serializers.CharField(help_text=f"`list_c_system_type` of template, Hệ thống {METADATA_SYSTEM_TYPE_LIST}")


class TemplateListSerializer(InheritedSerializer):
    item = TemplateListItemSerializer(many=True)
    start_date = serializers.DateField(
        help_text="`start_date` of template, `Ngày bắt đầu` nhỏ nhất trong list item")
    end_date = serializers.DateField(
        help_text="`end_date` of template, `Ngày kết thúc` lớn nhất trong list item")
    total_page = serializers.IntegerField(help_text="`total_page` of template")
    total_record = serializers.IntegerField(
        help_text="`total_record` of template")
    page = serializers.IntegerField(help_text="`page` of template")


class TemplateCheckExistCodeRequestSerializer(InheritedSerializer):
    code = serializers.CharField(help_text="`code` of template")


class TemplateCheckExistCodeResponseSerializer(InheritedSerializer):
    is_exist = serializers.BooleanField(help_text="`is_exist` of code in template . Nếu true thì code đã tồn tại")
