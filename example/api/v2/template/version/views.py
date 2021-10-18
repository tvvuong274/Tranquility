from api.base.base_views import BaseAPIView
from api.base.serializers import ExceptionResponseSerializer

from drf_spectacular.utils import extend_schema
from rest_framework import status

from django.db.models import Q

from db_models.template.models import Template

from api.v2.template.version.serializers import VersionResponseSerializer
from api.v2.template.version.schemas import EXAMPLE_RESPONSE_LIST_VERSION_SUCCESS


class VersionView(BaseAPIView):
    @extend_schema(
        operation_id='version-list',
        summary='List',
        tags=["Version"],
        description='Version template',
        responses={
            status.HTTP_200_OK: VersionResponseSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_VERSION_SUCCESS
        ]
    )
    def list_version(self, request, template_id):
        template = self.get_model_object_by_id(id=template_id, model=Template)

        versions = Template.objects.filter(Q(id=template_id) | Q(id__in=template.list_child_version_id)).values(
            'id',
            'code',
            'name',
            'version',
            'start_date',
            'end_date',
            'updated_by'
        ).order_by('-id')

        return self.response_success(list(versions))
