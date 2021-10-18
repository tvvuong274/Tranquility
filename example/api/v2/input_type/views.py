from drf_spectacular.utils import extend_schema
from rest_framework import status
from api.base.base_views import BaseAPIView
from api.base.serializers import ExceptionResponseSerializer
from api.v2.input_type.schemas import EXAMPLE_RESPONSE_LIST_INPUT_TYPE_SUCCESS, \
    EXAMPLE_RESPONSE_LIST_FORMAT_OF_AN_INPUT_TYPE_SUCCESS, \
    EXAMPLE_RESPONSE_JSON_CONDITION_OF_AN_INPUT_TYPE_FORMAT_SUCCESS
from api.v2.input_type.serializers import InputTypeListSuccessResponseSerializer, \
    InputTypeFormatListSuccessResponseSerializer, InputTypeFormatConditionListSuccessResponseSerializer
from library.constant.input_type import INPUT_TYPE, INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE, INPUT_TYPE_FORMAT, \
    INPUT_TYPE_FORMAT_CONDITION


class InputTypeView(BaseAPIView):
    @extend_schema(
        operation_id='input-type-list',
        summary='List',
        tags=["Input Type"],
        description='List all input types',
        responses={
            status.HTTP_200_OK: InputTypeListSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_INPUT_TYPE_SUCCESS,
        ]
    )
    def list(self, request):
        data = [{
            'id': input_type_id,
            'name': input_type_name,
            'total_used': 0,
        } for input_type_id, input_type_name in INPUT_TYPE.items()]
        return self.response_success(data, status_code=status.HTTP_200_OK)

    @extend_schema(
        operation_id='input-type-format-list',
        summary='List format',
        tags=["Input Type"],
        description='List all formats of an input type',
        responses={
            status.HTTP_200_OK: InputTypeFormatListSuccessResponseSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_FORMAT_OF_AN_INPUT_TYPE_SUCCESS,
        ]
    )
    def list_format(self, request, input_type_id):
        if input_type_id not in INPUT_TYPE:
            return self.http_exception(description=f'input_type_id={input_type_id} is not exist')

        input_type_formats = []
        for input_type_format_id in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[input_type_id]:
            input_type_formats.append({
                'id': input_type_format_id,
                'description': INPUT_TYPE_FORMAT[input_type_format_id],
                'conditions': INPUT_TYPE_FORMAT_CONDITION[input_type_format_id]
            })

        return self.response_success(input_type_formats, status_code=status.HTTP_200_OK)

    @extend_schema(
        operation_id='input-type-format-condition-json',
        summary='Json condition',
        tags=["Input Type"],
        description='Get detail json condition of an input type format',
        responses={
            status.HTTP_200_OK: InputTypeFormatConditionListSuccessResponseSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_JSON_CONDITION_OF_AN_INPUT_TYPE_FORMAT_SUCCESS,
        ]
    )
    def json_condition(self, request, input_type_id, input_type_format_id):
        if input_type_id not in INPUT_TYPE:
            return self.http_exception(description=f'input_type_id={input_type_id} is not exist')

        if input_type_format_id not in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[input_type_id]:
            return self.http_exception(description=f'input_type_format_id={input_type_format_id} is not exist')

        return self.response_success(INPUT_TYPE_FORMAT_CONDITION[input_type_format_id], status_code=status.HTTP_200_OK)
