from rest_framework import serializers
from api.base.serializers import InheritedSerializer


class MetadataCreateUpdateRequestSerializer(InheritedSerializer):
    code = serializers.CharField(
        help_text="`code` of metadata",
        allow_null=False, required=True
    )
    name = serializers.CharField(
        help_text="`name` of metadata",
        allow_null=False, required=True
    )
    list_c_system_type = serializers.ListField(
        help_text="`system_type` of metadata. In range[1:3) with 1=CRM, 2=LOS, 3=HRM",
        allow_null=False, required=True
    )
    active_flag = serializers.BooleanField(
        help_text="`active_flag` of metadata",
        allow_null=False, required=True
    )
    note = serializers.CharField(
        help_text="`note` of metadata",
        allow_null=True, required=True
    )
    output_edit_flag = serializers.BooleanField(
        help_text="`output_edit_flag` of metadata",
        allow_null=False, required=True
    )
    metadata_group_id = serializers.IntegerField(
        help_text="`metadata_group_id` of metadata_group",
        allow_null=False, required=True
    )
    # input_condition_json = serializers.JSONField(
    #     help_text="`input_condition_json` of metadata_group",
    #     allow_null=False, required=True
    # )
    input_type_format_id = serializers.IntegerField(
        help_text="`input_type_format_id` of metadata",
        allow_null=False, required=True
    )


class MetadataCreateSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of metadata")
    name = serializers.CharField(help_text="`name` of metadata")
    created_by = serializers.CharField(help_text="`created_by` of metadata")


class MetadataUpdateSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id update` of metadata")
    created_by = serializers.CharField(help_text="`created_by` of metadata")
    updated_by = serializers.CharField(help_text="`updated_by` of metadata")


class MetadataListItemResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of metadata")
    name = serializers.CharField(help_text="`name` of metadata")
    code = serializers.CharField(help_text="`code` of metadata, Code là ID trong Thông tin Metadata")
    input_type_name = serializers.CharField(help_text="`Tên loại nhập liệu`")
    number_template = serializers.IntegerField(help_text="`Số biểu mẫu sử dụng`")
    list_c_system_type = serializers.ListField(help_text="`list_c_system_type` of metadata")
    list_system_type_name = serializers.ListField(help_text="`Hệ thống sử dụng`")
    metadata_group_id = serializers.IntegerField(help_text="`metadata_group_id` of metadata_group")
    metadata_group_name = serializers.CharField(help_text="`Tên nhóm metadata`")
    active_flag = serializers.BooleanField(help_text="`active_flag` of metadata, Trạng thái")


class MetadataListResponseSerializer(InheritedSerializer):
    item = MetadataListItemResponseSerializer(many=True)
    total_page = serializers.IntegerField(help_text="`total_page` of metadata")
    total_record = serializers.IntegerField(help_text="`total_record` of metadata")
    page = serializers.IntegerField(help_text="`page` of metadata")


class MetadataDetailSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of metadata")
    name = serializers.CharField(help_text="`name` of metadata")
    code = serializers.CharField(help_text="`code` of metadata, Code là ID trong Thông tin Metadata")
    note = serializers.CharField(help_text="`note` of metadata")
    active_flag = serializers.BooleanField(help_text="`active_flag` of metadata, Trạng thái")
    output_edit_flag = serializers.BooleanField(help_text="`data_input_flag` of metadata")
    list_c_system_type = serializers.ListField(help_text="`list_c_system_type` of metadata")
    input_type_format_id = serializers.IntegerField(help_text="`input_type_format_id` of metadata")
    input_condition_json = serializers.JSONField(help_text="`input_condition_json` of metadata")
    metadata_group_id = serializers.IntegerField(help_text="`metadata_group_id` of metadata_group")


class MetadataListRequestSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` of metadata", allow_null=True, required=False, default=None)
    input_type_id = serializers.IntegerField(
        help_text="`id` of input_type", allow_null=True, required=False, default=None
    )
    active_flag = serializers.BooleanField(
        help_text="`active flag` of metadata", allow_null=True, required=False, default=None
    )
    list_c_system_type = serializers.ListField(
        help_text="`system_type` of metadata . In range[1:3] with 1=CRM, 2=LOS, 3=HRM", allow_null=True, required=False,
        default=None
    )


class MetadataListMetadataGroupResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="`id` of metadata group")
    name = serializers.CharField(help_text="`name` of metadata group")


class MetadataCheckExistCodeRequestSerializer(InheritedSerializer):
    code = serializers.CharField(help_text="`code` of metadata")


class MetadataCheckExistCodeResponseSerializer(InheritedSerializer):
    is_exist = serializers.BooleanField(help_text="`is_exist` of code in metadata . Nếu true thì code đã tồn tại")
