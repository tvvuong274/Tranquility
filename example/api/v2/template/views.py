from library.constant.metadata import METADATA_SYSTEM_TYPE
from re import T
from rest_framework.response import Response
from library.constant.template import (
    TEMPLATE_DEFAULT_SORT, 
    TEMPLATE_DEFAULT_SORT_A_TO_Z
)
from library.functions import (
    date_to_datetime,
    datetime_to_date, 
    end_time_of_day, 
    string_to_datetime
)
from idm_config.settings import DATE_INPUT_FORMAT
from api.v2.template.schemas import (
    EXAMPLE_RESPONSE_LIST_TEMPLATE_SUCCESS, 
    PARAMETER_LIST_TEMPLATE,
    PARAMETER_REQUEST_CHECK_CODE_TEMPLATE
)
from api.v2.template.serializers import (
    TemplateListItemSerializer, 
    TemplateListSerializer, 
    TemplateSearchSerializer,
    TemplateCheckExistCodeRequestSerializer,
    TemplateCheckExistCodeResponseSerializer
)
from api.base.serializers import ExceptionResponseSerializer
from rest_framework import status
from api.base.base_views import BaseAPIView
from drf_spectacular.utils import extend_schema
from db_models.template.models import Template


class TemplateView(BaseAPIView):
    @extend_schema(
        operation_id="Template-List",
        summary="List",
        tags=["Template"],
        description="List Template",
        parameters=PARAMETER_LIST_TEMPLATE,
        responses={
            status.HTTP_200_OK: TemplateListSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_TEMPLATE_SUCCESS,
        ],
    )
    def list(self, request):

        serializer = TemplateSearchSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        template_folder_id = serializer.validated_data['template_folder_id']

        templates = Template.objects.filter(
            template_folder=template_folder_id,
            #Version mới nhất: parent_id là Null
            #Version cũ: parent_id là id của version mới sau nó
            parent_id=None,    
        ).values(
            'id',
            'name', 
            'version', 
            'start_date', 
            'end_date', 
            'updated_by', 
            'updated_at', 
            'c_status', 
            'list_c_system_type',
            'list_child_version_id',
        ).order_by('name')

        # Tìm kiếm
        name = serializer.validated_data["name"]
        if name is not None:
            templates = templates.filter(name__icontains=name)

        sort = serializer.validated_data["sort"]
        # Nếu sort không nằm trong danh sách định nghĩa
        if sort not in TEMPLATE_DEFAULT_SORT:
            return self.http_exception(description=f"Sort not in {TEMPLATE_DEFAULT_SORT}")
        # Nếu sort khác mặc định A-Z
        if sort != TEMPLATE_DEFAULT_SORT_A_TO_Z:
            templates = templates.order_by('-name')

        start_date = serializer.validated_data["start_date"]
        end_date = serializer.validated_data["end_date"]

        start_date = date_to_datetime(start_date)
        end_date = end_time_of_day(date_to_datetime(end_date))

        # Ngày bắt đầu <= Ngày kết thúc => raise lỗi
        if start_date > end_date:
            return self.http_exception(description="start_date is greater than end_date")

        templates = templates.filter(
            start_date__gte=start_date, start_date__lte=end_date, 
            end_date__gte=start_date, end_date__lte=end_date
        )
        self.paginate(templates)

        # Chuyển datetime sang date cho output
        min_start_date = self.paging_list[0]['start_date']
        max_end_date = self.paging_list[0]['end_date']
        for template in self.paging_list:
            # Tìm ngày bắt đầu nhỏ nhất
            if template["start_date"] < min_start_date:
                min_start_date = template["start_date"]
            # Tìm ngày kết thúc nhất
            if template["end_date"] > max_end_date:
                max_end_date = template["end_date"]

            template["start_date"] = datetime_to_date(template["start_date"])

            template['list_system_type_name'] = [METADATA_SYSTEM_TYPE[c_system_type]
                                                 for c_system_type in template['list_c_system_type']]
        
        response = TemplateListItemSerializer(self.paging_list, many=True)
        # Start_date nhỏ nhất, End_date lớn nhất
        response_paging_data = self.response_paging(response.data).data
        response_paging_data.update({
            'start_date': datetime_to_date(min_start_date),
            'end_date': datetime_to_date(max_end_date),
        })

        return Response(response_paging_data)

    @extend_schema(
        operation_id='Template-check-code',
        summary='Check exist code',
        tags=["Template"],
        description='Template check code',
        parameters=PARAMETER_REQUEST_CHECK_CODE_TEMPLATE,
        responses={
            status.HTTP_200_OK: TemplateCheckExistCodeResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def check_exist(self, request):
        serializer = TemplateCheckExistCodeRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        is_exist = Template.objects.filter(code=serializer.validated_data['code']).exists()

        return self.response_success({
            "is_exist": is_exist
        }, status_code=status.HTTP_200_OK)
