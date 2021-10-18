from rest_framework import serializers
from api.base.serializers import InheritedSerializer


class DataSourceApiCreateUpdateRequestSerializer(InheritedSerializer):
    name = serializers.CharField(
        help_text="`name` of data source api",
        allow_null=False, required=True
    )
    c_method_type = serializers.IntegerField(
        help_text="`method type` of data source api",
        allow_null=False, required=True
    )
    url = serializers.CharField(
        help_text="`url` of data source api",
        allow_null=False, required=True
    )
    c_auth_type = serializers.IntegerField(
        help_text="`auth type` of data source api",
        allow_null=False, required=True
    )
    auth_json = serializers.JSONField(
        help_text="`token` if `c_auth_type` is `bearer token`; `username, password` if `c_auth_type` is `basic auth`",
        allow_null=False, required=True
    )
    header_list = serializers.JSONField(
        help_text="`header list` of data source api (json include 3 key: `key`, `value`, `description`) ",
        allow_null=False, required=True
    )
    body_json = serializers.JSONField(
        help_text="`body json` of data source api",
        allow_null=False, required=True
    )


class DataSourceApiCreateUpdateSuccessResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="id of data source api")
    name = serializers.CharField(help_text="name of data source api")
    template_id = serializers.IntegerField(help_text="id of template")


class DataSourceApiListTemplateResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="id of template data source api")
    data_source_api_id = serializers.CharField(help_text="id of data source api")
    data_source_api_name = serializers.CharField(help_text="name of data source api")


class DataSourceApiListAllResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(help_text="id of data source api")
    name = serializers.CharField(help_text="name of data source api")


class DataSourceApiDetailResponseSerializer(InheritedSerializer):
    id = serializers.IntegerField(
        help_text="`id` of data source api",
        allow_null=False, required=True
    )
    name = serializers.CharField(
        help_text="`name` of data source api",
        allow_null=False, required=True
    )
    c_method_type = serializers.IntegerField(
        help_text="`method type` of data source api",
        allow_null=False, required=True
    )
    url = serializers.CharField(
        help_text="`url` of data source api",
        allow_null=False, required=True
    )
    c_auth_type = serializers.IntegerField(
        help_text="`auth type` of data source api",
        allow_null=False, required=True
    )
    auth_json = serializers.JSONField(
        help_text="`token` if `c_auth_type` is `bearer token`; `username, password` if `c_auth_type` is `basic auth`",
        allow_null=False, required=True
    )
    header_list = serializers.JSONField(
        help_text="`header list` of data source api (json include 3 key: `key`, `value`, `description`) ",
        allow_null=False, required=True
    )
    body_json = serializers.JSONField(
        help_text="`body json` of data source api",
        allow_null=False, required=True
    )


class DataSourceApiCopyRequestSerializer(InheritedSerializer):
    template_id = serializers.IntegerField(
        help_text="`id` of template",
        allow_null=False, required=True
    )
