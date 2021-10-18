from api.base.base_views import BaseAPIView
from api.base.serializers import ExceptionResponseSerializer

from rest_framework import status
from drf_spectacular.utils import extend_schema

from db_models.organization.block.models import Block
from db_models.organization.department.models import Department

from api.v2.organization.serializers import (
    BlockListResponseSerializer,
    DepartmentListResponseSerializer
)
from api.v2.organization.schemas import (
    EXAMPLE_RESPONSE_LIST_BLOCK_SUCCESS,
    EXAMPLE_RESPONSE_LIST_DEPARTMENT_SUCCESS
)


class OrganizationView(BaseAPIView):
    @extend_schema(
        operation_id='Block-list',
        summary='List block',
        tags=["Organization"],
        description='Block-list',
        responses={
            status.HTTP_200_OK: BlockListResponseSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_BLOCK_SUCCESS
        ]
    )
    def list_block(self, request):
        return self.response_success(list(Block.objects.order_by('id').values('id', 'name')))

    @extend_schema(
        operation_id='Department-list',
        summary='List department',
        tags=["Organization"],
        description='Department-list',
        responses={
            status.HTTP_200_OK: DepartmentListResponseSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_DEPARTMENT_SUCCESS
        ]
    )
    def list_department(self, request):
        return self.response_success(list(Department.objects.order_by('id').values('id', 'name')))