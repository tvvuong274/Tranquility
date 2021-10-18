from api.base.base_views import BaseAPIView
from api.base.serializers import ExceptionResponseSerializer

from drf_spectacular.utils import extend_schema
from rest_framework import status

from functools import reduce
import operator
from django.db.models import Q, F, Subquery, OuterRef, Count
from api.functions.input_type.functions import is_valid_input_type_text_format_condition, \
    is_valid_input_type_one_or_multiple_choice_format_condition, is_valid_input_type_media_format_condition, \
    is_valid_input_type_document_format_condition, is_valid_input_type_range_format_condition, \
    is_valid_input_type_rating_format_condition
from db_models.metadata.group.models import MetadataGroup
from db_models.metadata.models import Metadata
from db_models.template.field.models import TemplateField
from db_models.metadata.comment.models import MetadataComment

from library.constant.metadata import METADATA_SYSTEM_TYPE
from library.constant.file_extension import (
    FILE_EXTENSION_IMAGES,
    FILE_EXTENSION_VIDEOS,
    FILE_EXTENSION_SOUNDS
)
from library.constant.input_type import (
    INPUT_INPUT_TYPE_DOCUMENT,
    INPUT_INPUT_TYPE_MEDIA,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE_CONDITION_JSON,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND_CONDITION_JSON,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO_CONDITION_JSON,
    INPUT_INPUT_TYPE_ONE_CHOICE,
    INPUT_INPUT_TYPE_MULTI_CHOICE,
    INPUT_INPUT_TYPE_RANGE,
    INPUT_INPUT_TYPE_RATING,
    INPUT_TYPE_FORMAT,
    INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE,
    INPUT_INPUT_TYPE_TEXT,
    INPUT_TYPE
)
from api.v2.metadata.serializers import (
    MetadataCreateUpdateRequestSerializer,
    MetadataCreateSuccessResponseSerializer,
    MetadataUpdateSuccessResponseSerializer,
    MetadataDetailSuccessResponseSerializer,
    MetadataListResponseSerializer,
    MetadataListItemResponseSerializer,
    MetadataListRequestSerializer,
    MetadataListMetadataGroupResponseSerializer,
    MetadataCheckExistCodeRequestSerializer,
    MetadataCheckExistCodeResponseSerializer
)
from api.v2.metadata.schemas import (
    EXAMPLE_RESPONSE_CREATE_METADATA_SUCCESS,
    EXAMPLE_RESPONSE_UPDATE_METADATA_SUCCESS,
    EXAMPLE_RESPONSE_DETAIL_METADATA_SUCCESS,
    EXAMPLE_RESPONSE_LIST_METADATA_SUCCESS,
    PARAMETER_REQUEST_LIST_METADATA,
    EXAMPLE_RESPONSE_LIST_METADATA_GROUP_SUCCESS,
    PARAMETER_REQUEST_CHECK_CODE_METADATA,
)


class MetadataGroupView(BaseAPIView):
    @extend_schema(
        operation_id='metadata-list-group',
        summary='List',
        tags=["Metadata Group"],
        description='List group metadata',
        responses={
            status.HTTP_200_OK: MetadataListMetadataGroupResponseSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_METADATA_GROUP_SUCCESS
        ]
    )
    def list_group(self, request):
        return self.response_success(list(MetadataGroup.objects.order_by('id').values('id', 'name')))


class MetadataView(BaseAPIView):
    @extend_schema(
        operation_id='Metadata-list',
        summary='List',
        tags=["Metadata"],
        description='Metadata',
        parameters=PARAMETER_REQUEST_LIST_METADATA,
        responses={
            status.HTTP_200_OK: MetadataListResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_METADATA_SUCCESS,
        ]
    )
    def list(self, request):
        query_set_metadata = Metadata.objects.annotate(
            metadata_group_name=F('metadata_group__name'),
            number_template=Subquery(
                TemplateField.objects.filter(metadata_id=OuterRef('id')).values('metadata').annotate(
                    number_template=Count('id')
                ).values('number_template')
            ),
        ).values(
            'id',
            'name',
            'code',
            'input_type_format_id',
            'number_template',
            'list_c_system_type',
            'metadata_group_id',
            'metadata_group_name',
            'active_flag',
        ).order_by('id')
        
        serializer = MetadataListRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        name = serializer.validated_data['name']
        active_flag = serializer.validated_data['active_flag']
        list_c_system_type = serializer.validated_data['list_c_system_type']
        input_type_id = serializer.validated_data['input_type_id']

        if name is not None:
            query_set_metadata = query_set_metadata.filter(name__icontains=name)

        if active_flag is not None:
            query_set_metadata = query_set_metadata.filter(active_flag=active_flag)

        if input_type_id is not None:
            if input_type_id in INPUT_TYPE:
                input_type_format_ids = INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[input_type_id]
                query_set_metadata = query_set_metadata.filter(input_type_format_id__in=input_type_format_ids)
            else:
                return self.http_exception(description=f'input_type_id={input_type_id} is not exist')

        if list_c_system_type is not None:
            # Hàm sử dụng icontains chỉ áp dụng c_system_type thuộc trong khoãng [0:9).
            query = reduce(operator.or_, (Q(list_c_system_type__icontains=item) for item in list_c_system_type))
            query_set_metadata = query_set_metadata.filter(query)

        self.paginate(query_set_metadata)

        for metadata in self.paging_list:
            for input_type_id, input_type_format_ids in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE.items():
                if metadata['input_type_format_id'] in input_type_format_ids:
                    metadata['input_type_name'] = INPUT_TYPE[input_type_id]
                    break

            metadata['number_template'] = metadata['number_template'] if metadata['number_template'] else 0

            metadata['list_system_type_name'] = [METADATA_SYSTEM_TYPE[c_system_type]
                                                 for c_system_type in metadata['list_c_system_type']]

        serializer_metadata_response = MetadataListItemResponseSerializer(self.paging_list, many=True)

        return self.response_paging(serializer_metadata_response.data)

    @extend_schema(
        operation_id='metadata-detail',
        summary='Detail',
        tags=["Metadata"],
        description='Detail a metadata',
        responses={
            status.HTTP_200_OK: MetadataDetailSuccessResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_DETAIL_METADATA_SUCCESS
        ]
    )
    def detail_metadata(self, request, metadata_id):
        metadata = self.get_model_object_by_id(id=metadata_id, model=Metadata)

        output = {
            'id': metadata_id,
            'name': metadata.name,
            'code': metadata.code,
            'note': metadata.note,
            'active_flag': metadata.active_flag,
            'list_c_system_type': metadata.list_c_system_type,
            'output_edit_flag': metadata.output_edit_flag,
            'input_type_format_id': metadata.input_type_format_id,
            'input_condition_json': metadata.input_condition_json,
            'metadata_group_id': metadata.metadata_group_id,
        }
        return self.response_success(output, status_code=status.HTTP_200_OK)

    def _is_valid_input_type(self, input_type_format_id, json_condition):
        INPUT_TYPE_FORMAT_ONE_OR_MUL_CHOICE = INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_ONE_CHOICE] + \
                                              INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_MULTI_CHOICE]
        message = "JSON format not true"

        if input_type_format_id in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_TEXT]:  # [1, 2]
            if not is_valid_input_type_text_format_condition(json_condition):
                return self.http_exception(description=message)

        elif input_type_format_id in INPUT_TYPE_FORMAT_ONE_OR_MUL_CHOICE:  # [3, 4, 5, 6]
            if not is_valid_input_type_one_or_multiple_choice_format_condition(json_condition):
                return self.http_exception(description=message)

        elif input_type_format_id in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_MEDIA]:  # [12, 13, 14]
            if input_type_format_id == INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE:

                if not is_valid_input_type_media_format_condition(
                        json_condition,
                        INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE_CONDITION_JSON, FILE_EXTENSION_IMAGES):
                    return self.http_exception(description=message)

                elif input_type_format_id == INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO:
                    if not is_valid_input_type_media_format_condition(
                            json_condition,
                            INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO_CONDITION_JSON, FILE_EXTENSION_VIDEOS):
                        return self.http_exception(description=message)

                elif input_type_format_id == INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND:
                    if not is_valid_input_type_media_format_condition(
                            json_condition,
                            INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND_CONDITION_JSON, FILE_EXTENSION_SOUNDS):
                        return self.http_exception(description=message)

        elif input_type_format_id in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_DOCUMENT]:  # [15, 16, 17]
            if not is_valid_input_type_document_format_condition(json_condition):
                return self.http_exception(description=message)

        elif input_type_format_id in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_RANGE]:  # [20]
            if not is_valid_input_type_range_format_condition(json_condition):
                return self.http_exception(description=message)

        elif input_type_format_id in INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE[INPUT_INPUT_TYPE_RATING]:  # [18, 19]
            if not is_valid_input_type_rating_format_condition(json_condition):
                return self.http_exception(description=message)
        else:
            if len(json_condition) > 0:
                return self.http_exception(description="JSON should be empty. Not condition in this type.")

    @extend_schema(
        operation_id='Metadata-Create',
        summary='Create',
        tags=["Metadata"],
        description='Create new metadata',
        request=MetadataCreateUpdateRequestSerializer,
        responses={
            status.HTTP_201_CREATED: MetadataCreateSuccessResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer
        },
        examples=[
            EXAMPLE_RESPONSE_CREATE_METADATA_SUCCESS,
        ]
    )
    def create(self, request):
        serializer = MetadataCreateUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data['code']
        if Metadata.objects.filter(code__exact=code).exists():
            return self.http_exception(description='code already exists')

        list_c_system_type = serializer.validated_data['list_c_system_type']
        for c_system_type in list_c_system_type:
            if c_system_type not in METADATA_SYSTEM_TYPE:
                return self.http_exception(description='list_c_system_type is not METADATA_SYSTEM_TYPE')

        input_type_format_id = serializer.validated_data['input_type_format_id']
        if input_type_format_id not in INPUT_TYPE:
            return self.http_exception(description='INPUT_TYPE not in INPUT_TYPE constant')
        
        # hiện tại chưa làm tính năng chọn format và condition nên tạm khai báo bằng dict rỗng
        input_condition_json = {}
        # input_condition_json = serializer.validated_data['input_condition_json']
        # self._is_valid_input_type(input_type_format_id, input_condition_json)
        
        metadata_group_id = serializer.validated_data['metadata_group_id']
        self.get_model_object_by_id(id=metadata_group_id, model=MetadataGroup)

        metadata = Metadata.objects.create(
            code=code,
            name=serializer.validated_data['name'],
            note=serializer.validated_data['note'],
            list_c_system_type=list_c_system_type,
            active_flag=serializer.validated_data['active_flag'],
            output_edit_flag=serializer.validated_data['output_edit_flag'],
            input_type_format_id=input_type_format_id,
            input_condition_json=input_condition_json,
            metadata_group_id=metadata_group_id,
            created_by=self.user.name,
            updated_by=self.user.name
        )

        content = f"Đã tạo {metadata.name}"

        MetadataComment.objects.create(
            metadata_id=metadata.id,
            user_id=self.user.id,
            log_flag=True,
            content=content,
            created_by=self.user.name,
            updated_by=self.user.name
        )

        return self.response_success({
            'id': metadata.id,
            'name': metadata.name,
            'created_by': metadata.created_by
        }, status_code=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id='metadata-Update',
        summary='Update',
        tags=["Metadata"],
        description='Update metadata',
        request=MetadataCreateUpdateRequestSerializer,
        responses={
            status.HTTP_200_OK: MetadataUpdateSuccessResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer
        },
        examples=[
            EXAMPLE_RESPONSE_UPDATE_METADATA_SUCCESS,
        ]
    )
    def update(self, request, metadata_id):
        serializer = MetadataCreateUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        metadata = self.get_model_object_by_id(id=metadata_id, model=Metadata)

        content_list = []

        name = serializer.validated_data['name']
        if name != metadata.name:
            content_list.append(f"Thay đổi name metadata từ {metadata.name} thành {name}")

        note = serializer.validated_data['note']
        if note != metadata.note:
            content_list.append(f"Thay đổi note metadata từ {metadata.note} thành {note}")

        active_flag = serializer.validated_data['active_flag']
        if active_flag != metadata.active_flag:
            content_list.append(f"Thay đổi active_flag metadata từ {metadata.active_flag} thành {active_flag}")

        output_edit_flag = serializer.validated_data['output_edit_flag']
        if output_edit_flag != metadata.output_edit_flag:
            content_list.append(f"Thay đổi output_edit_flag metadata "
                                f"từ {metadata.output_edit_flag} thành {output_edit_flag}")

        code = serializer.validated_data['code']
        if code != metadata.code:
            content_list.append(f"Thay đổi code metadata từ {metadata.code} thành {code}")
            if Metadata.objects.filter(code__exact=code).exists():
                return self.http_exception(description='code already exists')

        list_c_system_type = serializer.validated_data['list_c_system_type']
        if list_c_system_type != metadata.list_c_system_type:
            content_list.append(f"Thay đổi list_c_system_type metadata "
                                f"từ {metadata.list_c_system_type} thành {list_c_system_type}")
            for c_system_type in list_c_system_type:
                if c_system_type not in METADATA_SYSTEM_TYPE:
                    return self.http_exception(description='list_c_system_type is not METADATA_SYSTEM_TYPE')

        input_type_format_id = serializer.validated_data['input_type_format_id']
        if input_type_format_id != metadata.input_type_format_id:
            content_list.append(f"Thay đổi input_type metadata "
                                f"từ {metadata.input_type_format_id} thành {input_type_format_id}")
            if input_type_format_id not in INPUT_TYPE:
                return self.http_exception(description='INPUT_TYPE not in INPUT_TYPE constant')

        # hiện tại chưa làm tính năng chọn format và condition nên tạm khai báo bằng dict rỗng
        input_condition_json = {}
        # input_condition_json = serializer.validated_data['input_condition_json']
        # if input_condition_json != metadata.input_condition_json:
        #     self._is_valid_input_type(input_type_format_id, input_condition_json)

        metadata_group_id = serializer.validated_data['metadata_group_id']
        if metadata_group_id != metadata.metadata_group_id:
            content_list.append(f"Thay đổi metadata_group metadata từ {metadata.metadata_group_id} thành {metadata_group_id}")
            self.get_model_object_by_id(id=metadata_group_id, model=MetadataGroup)

        metadata.code = code
        metadata.name = name
        metadata.note = note
        metadata.list_c_system_type = list_c_system_type
        metadata.active_flag = active_flag
        metadata.output_edit_flag = output_edit_flag
        metadata.input_type_format_id = input_type_format_id
        metadata.input_condition_json = input_condition_json
        metadata.metadata_group_id = metadata_group_id

        metadata.updated_by = self.user.name

        metadata.save()

        content = '\n'.join(content_list)
        
        MetadataComment.objects.create(
            metadata_id=metadata.id,
            user_id=self.user.id,
            log_flag=True,
            content=content,
            created_by=self.user.name,
            updated_by=self.user.name
        )
        
        return self.response_success({
            "id": metadata.id,
            "created_by": metadata.created_by,
            "updated_by": metadata.updated_by
        }, status_code=status.HTTP_200_OK)

    @extend_schema(
        operation_id='metadata-delete',
        summary='Delete',
        tags=["Metadata"],
        description='Delete a metadata',
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def delete(self, request, metadata_id):
        metadata = self.get_model_object_by_id(id=metadata_id, model=Metadata)

        # Kiểm tra ràng buộc nếu metadata được sử dụng thì không được xóa
        if TemplateField.objects.filter(metadata=metadata).exists():
            return self.http_exception("Delete Template Field before delete Metadata")

        metadata.delete()

        return self.response_success(None, status_code=status.HTTP_204_NO_CONTENT)
    
    @extend_schema(
        operation_id='Metadata-check-code',
        summary='Check exist code',
        tags=["Metadata"],
        description='Metadata check code',
        parameters=PARAMETER_REQUEST_CHECK_CODE_METADATA,
        responses={
            status.HTTP_200_OK: MetadataCheckExistCodeResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def check_exist(self, request):
        serializer = MetadataCheckExistCodeRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        is_exist = Metadata.objects.filter(code=serializer.validated_data['code']).exists()

        return self.response_success({
            "is_exist": is_exist
        }, status_code=status.HTTP_200_OK)