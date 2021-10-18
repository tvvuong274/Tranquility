from urllib import parse

from django.db.models import F
from drf_spectacular.utils import extend_schema
from rest_framework import status

from api.base.base_views import BaseAPIView
from api.base.serializers import ExceptionResponseSerializer
from api.v2.data_source_api.schemas import (
    EXAMPLE_RESPONSE_CREATE_DATA_SOURCE_API,
    EXAMPLE_RESPONSE_UPDATE_DATA_SOURCE_API, EXAMPLE_RESPONSE_LIST_ALL_DATA_SOURCE_API_SUCCESS,
    EXAMPLE_RESPONSE_DETAIL_DATA_SOURCE_API, PARAMETER_REQUEST_DATA_SOURCE_API,
    EXAMPLE_REQUEST_BEARER_TOKEN_CREATE_UPDATE_DATA_SOURCE_API,
    EXAMPLE_REQUEST_BASIC_AUTH_CREATE_UPDATE_DATA_SOURCE_API,
    EXAMPLE_RESPONSE_LIST_DATA_SOURCE_API_OF_TEMPLATE_SUCCESS, EXAMPLE_RESPONSE_COPY_DATA_SOURCE_API
)
from api.v2.data_source_api.serializers import (
    DataSourceApiCreateUpdateRequestSerializer,
    DataSourceApiDetailResponseSerializer,
    DataSourceApiCopyRequestSerializer,
    DataSourceApiCreateUpdateSuccessResponseSerializer,
    DataSourceApiListAllResponseSerializer,
    DataSourceApiListTemplateResponseSerializer
)
from db_models.data_source_api.models import DataSourceAPI
from db_models.template.data_source_api.models import TemplateDataSourceAPI
from db_models.template.field.group.models import TemplateFieldGroup
from db_models.template.field.models import TemplateField
from db_models.template.models import Template
from library.constant.output_api import OUTPUT_API_METHOD_TYPE, OUTPUT_AUTHORIZATION_API_TYPE, \
    OUTPUT_AUTHORIZATION_API_TYPE_BEARER_TOKEN
from library.functions import is_valid_url


class DataSourceApiView(BaseAPIView):
    # @staticmethod
    # def _is_auth_json(c_auth_type, auth_json):
    #     if c_auth_type == OUTPUT_AUTHORIZATION_API_TYPE_BEARER_TOKEN:
    #         key_from_user = list(auth_json.keys())[0]
    #         if len(auth_json) != 1 or key_from_user != 'token':
    #             return False
    #     else:
    #         keys_auth_json = {'username', 'password'}
    #         keys_auth_json_from_user = set(auth_json.keys())
    #
    #         if keys_auth_json != keys_auth_json_from_user:
    #             return False
    #
    #     return True
    #
    # @staticmethod
    # def _is_valid_header_list(list_header):
    #     list_key_header = []
    #     for header in list_header:
    #         list_key_header.extend(list(header.keys()))
    #     set_keys_header_list_from_user = set(list_key_header)
    #     set_key_header_list = {'key', 'value', 'description'}
    #     if set_key_header_list == set_keys_header_list_from_user:
    #         return True
    #     return False
    #
    # def _validate_create_update_data(self, template_id, data):
    #     self.get_model_object_by_id(id=template_id, model=Template)
    #
    #     serializer = DataSourceApiCreateUpdateRequestSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     c_method_type = serializer.validated_data['c_method_type']
    #     if c_method_type not in OUTPUT_API_METHOD_TYPE:
    #         return self.http_exception(description=f'{c_method_type} is not in OUTPUT_API_METHOD_TYPE (1:GET/2:POST)')
    #
    #     c_auth_type = serializer.validated_data['c_auth_type']
    #     if c_auth_type not in OUTPUT_AUTHORIZATION_API_TYPE:
    #         return self.http_exception(
    #             description=f'{c_auth_type} is not OUTPUT_AUTHORIZATION_API_TYPE(1:BASIC_AUTH/2:BEARER_TOKEN')
    #
    #     auth_json = serializer.validated_data['auth_json']
    #     if not self._is_auth_json(c_auth_type=c_auth_type, auth_json=auth_json):
    #         return self.http_exception(description="auth_json is not valid")
    #
    #     # kiểm tra url
    #     url = serializer.validated_data['url']
    #     if not is_valid_url(url):
    #         return self.http_exception(description="url is wrong")
    #
    #     header_list = serializer.validated_data['header_list']
    #     if not self._is_valid_header_list(header_list):
    #         return self.http_exception(description="key in json header is wrong")
    #
    #     return serializer
    #
    # @staticmethod
    # def _split_endpoint_and_parameters(url):
    #     list_url_and_parameter = []
    #     if "?" not in url:
    #         parameter_list = {}
    #         origin_url = url
    #     else:
    #         parameter_list = dict(parse.parse_qsl(parse.urlsplit(url).query))
    #
    #         list_url = url.split('?')
    #         origin_url = list_url[0]
    #
    #     list_url_and_parameter.append(origin_url)
    #     list_url_and_parameter.append(parameter_list)
    #     return list_url_and_parameter
    #
    # @extend_schema(
    #     operation_id='data-source-api-create',
    #     summary='Create',
    #     tags=['DataSourceApi'],
    #     description='Create a data source api',
    #     request=DataSourceApiCreateUpdateRequestSerializer,
    #     responses={
    #         status.HTTP_201_CREATED: DataSourceApiCreateUpdateSuccessResponseSerializer,
    #         status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer
    #     },
    #     examples=[
    #         EXAMPLE_REQUEST_BEARER_TOKEN_CREATE_UPDATE_DATA_SOURCE_API,
    #         EXAMPLE_REQUEST_BASIC_AUTH_CREATE_UPDATE_DATA_SOURCE_API,
    #         EXAMPLE_RESPONSE_CREATE_DATA_SOURCE_API
    #     ]
    #
    # )
    # def create(self, request, template_id):
    #     serializer = self._validate_create_update_data(template_id=template_id, data=request.data)
    #
    #     list_url_and_parameter = self._split_endpoint_and_parameters(serializer.validated_data['url'])
    #     endpoint = list_url_and_parameter[0]
    #     parameter_list = list_url_and_parameter[1]
    #
    #     data_source_api = TemplateDataSourceAPI.objects.create(
    #         template_id=template_id,
    #         name=serializer.validated_data['name'],
    #         c_method_type=serializer.validated_data['c_method_type'],
    #         url=endpoint,
    #         c_auth_type=serializer.validated_data['c_auth_type'],
    #         auth_json=serializer.validated_data['auth_json'],
    #         header_list=serializer.validated_data['header_list'],
    #         parameter_list=parameter_list,
    #         body_json=serializer.validated_data['body_json'],
    #         created_by=self.user.name,
    #         updated_by=self.user.name,
    #     )
    #
    #     return self.response_success({
    #         'id': data_source_api.id,
    #         'name': data_source_api.name,
    #         "template_id": data_source_api.template_id,
    #         'created_by': data_source_api.created_by
    #     })
    #
    # @extend_schema(
    #     operation_id='data-source-api-update',
    #     summary='Update',
    #     tags=['DataSourceApi'],
    #     description='Update a data source api',
    #     request=DataSourceApiCreateUpdateRequestSerializer,
    #     responses={
    #         status.HTTP_200_OK: DataSourceApiCreateUpdateSuccessResponseSerializer,
    #         status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer
    #     },
    #     examples=[
    #         EXAMPLE_REQUEST_BEARER_TOKEN_CREATE_UPDATE_DATA_SOURCE_API,
    #         EXAMPLE_REQUEST_BASIC_AUTH_CREATE_UPDATE_DATA_SOURCE_API,
    #         EXAMPLE_RESPONSE_UPDATE_DATA_SOURCE_API
    #     ]
    # )
    # def update(self, request, template_id, data_source_api_id):
    #     serializer = self._validate_create_update_data(template_id=template_id, data=request.data)
    #
    #     list_url_and_parameter = self._split_endpoint_and_parameters(serializer.validated_data['url'])
    #     endpoint = list_url_and_parameter[0]
    #     parameter_list = list_url_and_parameter[1]
    #
    #     data_source_api = self.get_model_object_by_id(id=data_source_api_id, model=TemplateDataSourceAPI)
    #
    #     data_source_api.template_id = template_id
    #     data_source_api.name = serializer.validated_data['name']
    #     data_source_api.c_method_type = serializer.validated_data['c_method_type']
    #     data_source_api.url = endpoint
    #     data_source_api.c_auth_type = serializer.validated_data['c_auth_type']
    #     data_source_api.auth_json = serializer.validated_data['auth_json']
    #     data_source_api.header_list = serializer.validated_data['header_list']
    #     data_source_api.parameter_list = parameter_list
    #     data_source_api.body_json = serializer.validated_data['body_json']
    #     data_source_api.updated_by = self.user.name
    #
    #     data_source_api.save()
    #
    #     return self.response_success({
    #         'id': data_source_api.id,
    #         'name': data_source_api.name,
    #         "template_id": data_source_api.template_id,
    #         'updated_by': data_source_api.updated_by
    #     })
    #
    @extend_schema(
        operation_id='data-source-api-list-in-a-template',
        summary='List data source api of template',
        tags=['DataSourceApi'],
        description='List data source api of template',
        responses={
            status.HTTP_200_OK: DataSourceApiListTemplateResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_LIST_DATA_SOURCE_API_OF_TEMPLATE_SUCCESS]
    )
    def list_data_source_api_template(self, request, template_id):
        self.get_model_object_by_id(id=template_id, model=Template)

        list_data_source_api = TemplateDataSourceAPI.objects.annotate(
            data_source_api_name=F('data_source_api__name')
        ).filter(
            template_id=template_id
        ).values('id', 'data_source_api_id', 'data_source_api_name')

        return self.response_success(list(list_data_source_api), status_code=status.HTTP_200_OK)

    @extend_schema(
        operation_id='data-source-api-list-all',
        summary='List all data source api',
        tags=['DataSourceApi'],
        parameters=PARAMETER_REQUEST_DATA_SOURCE_API,
        description='List all data source api',
        responses={
            status.HTTP_200_OK: DataSourceApiListAllResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_LIST_ALL_DATA_SOURCE_API_SUCCESS]
    )
    def list_all_data_source_api(self, request):
        if request.query_params:
            name = request.query_params['name']
            list_data_source_api = DataSourceAPI.objects.filter(
                name__icontains=name
            ).values('id', 'name', )
        else:
            list_data_source_api = DataSourceAPI.objects.all().values('id', 'name')

        return self.response_success(list(list_data_source_api), status_code=status.HTTP_200_OK)

    @extend_schema(
        operation_id='data-source-api-detail',
        summary='Detail',
        tags=['DataSourceApi'],
        description='Detail a data source api',
        responses={
            status.HTTP_200_OK: DataSourceApiDetailResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_DETAIL_DATA_SOURCE_API]
    )
    def detail_data_source_api(self, request, data_source_api_id):

        data_source_api = self.get_model_object_by_id(id=data_source_api_id, model=DataSourceAPI)

        if not data_source_api.parameter_list:
            full_url = data_source_api.url
        else:
            parameter_strings = []
            for key, value in data_source_api.parameter_list.items():
                parameter_strings.append(f'{key}={value}')
            full_url = f'{data_source_api.url}?{"&".join(parameter_strings)}'

        output = {
            'id': data_source_api.id,
            'name': data_source_api.name,
            'c_method_type': data_source_api.c_method_type,
            'url': full_url,
            'c_auth_type': data_source_api.c_auth_type,
            'auth_json': data_source_api.auth_json,
            'header_list': data_source_api.header_list,
            'body_json': data_source_api.body_json
        }

        return self.response_success(output, status_code=status.HTTP_200_OK)

    # @extend_schema(
    #     operation_id='data-source-api-delete',
    #     summary='Delete',
    #     tags=['DataSourceApi'],
    #     description='Delete a data source api',
    #     responses={
    #         status.HTTP_204_NO_CONTENT: None,
    #         status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
    #         status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
    #     }
    # )
    # def delete(self, request, data_source_api_id, template_id):
    #     self.get_model_object_by_id(id=template_id, model=Template)
    #
    #     data_source_api = self.get_model_object_by_id(id=data_source_api_id, model=TemplateDataSourceAPI)
    #
    #     is_exist_template_field = TemplateField.objects.filter(template_data_source_api_id=data_source_api_id).exists()
    #     is_exist_template_field_group = TemplateFieldGroup.objects.filter(
    #         template_data_source_api_id=data_source_api_id).exists()
    #     if is_exist_template_field or is_exist_template_field_group:
    #         return self.http_exception(
    #             description="please delete template field or template group before delete data source api"
    #         )
    #
    #     data_source_api.delete()
    #
    #     return self.response_success(None, status_code=status.HTTP_204_NO_CONTENT)
    #
    @extend_schema(
        operation_id='data-source-api-copy',
        summary='Copy',
        tags=['DataSourceApi'],
        description='copy a data source api',
        request=DataSourceApiCopyRequestSerializer,
        responses={
            status.HTTP_201_CREATED: DataSourceApiCreateUpdateSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_COPY_DATA_SOURCE_API
        ]
    )
    def copy(self, request, data_source_api_id):
        serializer = DataSourceApiCopyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        template_id = serializer.validated_data['template_id']
        self.get_model_object_by_id(id=template_id, model=Template)

        self.get_model_object_by_id(id=data_source_api_id, model=DataSourceAPI)

        template_data_source_api = TemplateDataSourceAPI.objects.create(
            template_id=template_id,
            data_source_api_id=data_source_api_id,
            created_by=self.user.name,
            updated_by=self.user.name
        )

        return self.response_success({
            "id": template_data_source_api.id,
            "data_source_api_id": template_data_source_api.data_source_api_id,
            "template_id": template_data_source_api.template_id,
            "created_by": template_data_source_api.created_by,
            "updated_by": template_data_source_api.updated_by
        })
