from library.constant.message import MESSAGE_CODE_IS_EXISTED, MESSAGE_PARENT_IS_NOT_EXISTED, MESSAGE_SLUG_IS_EXISTED
from db_models.template.folder.models import TemplateFolder
from django.db.models import F
from api.v2.template_group.schemas import (
    EXAMPLE_RESPONSE_DETAIL_TEMPLATE_GROUP_SUCCESS,
    EXAMPLE_RESPONSE_LIST_MENU_TEMPLATE_GROUP_SUCCESS,
    EXAMPLE_RESPONSE_LIST_TEMPLATE_GROUP_SUCCESS,
    EXAMPLE_RESPONSE_UPDATE_TEMPLATE_GROUP_SUCCESS,
    PARAMETER_LIST_MENU_TEMPLATE_GROUP,
    PARAMETER_LIST_SEARCH_TEMPLATE_GROUP,
    PARAMETER_REQUEST_CHECK_CODE_OR_SLUG_TEMPLATE_GROUP
)
from db_models.template.group.models import TemplateGroup
from api.base.serializers import ExceptionResponseSerializer
from rest_framework import status
from api.v2.template_group.serializers import (
    TemplateGroupCreateSuccessSerializer,
    TemplateGroupDetailRequestSerializer,
    TemplateGroupDetailResponseSuccessSerializer,
    TemplateGroupListItemResponseSerializer,
    TemplateGroupListMenuResponseSuccessSerializer,
    TemplateGroupListResponseSuccessSerializer,
    TemplateGroupListSearchRequestSerializer,
    TemplateGroupMenuRequestSerializer,
    TemplateGroupRequestSerializer,
    TemplateGroupUpdateResponseSuccessSerializer,
    TemplateGroupCheckExistCodeRequestSerializer,
    TemplateGroupCheckExistCodeResponseSerializer
)
from drf_spectacular.utils import extend_schema
from api.base.base_views import BaseAPIView


class TemplateGroupView(BaseAPIView):
    @extend_schema(
        operation_id='Template-Group-Create',
        summary='Create',
        tags=["Template Group"],
        description='Create new Template Group',
        request=TemplateGroupRequestSerializer,
        responses={
            status.HTTP_201_CREATED: TemplateGroupCreateSuccessSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def create(self, request):
        serializer = TemplateGroupRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Kiểm tra code có tồn tại hay không, nếu có raise lỗi
        code = serializer.validated_data['code']
        if TemplateGroup.objects.filter(code=code).exists():
            self.http_exception(description=MESSAGE_CODE_IS_EXISTED)

        name = serializer.validated_data['name']

        # Kiểm tra slug có tồn tại hay không, nếu có raise lỗi
        slug = serializer.validated_data['slug']
        if TemplateGroup.objects.filter(slug=slug).exists():
            self.http_exception(description=MESSAGE_SLUG_IS_EXISTED)

        active_flag = serializer.validated_data['active_flag']

        # Kiểm tra parent có tồn tại hay không, nếu không raise lỗi
        parent_id = serializer.validated_data['parent_id']
        if parent_id is not None and not TemplateGroup.objects.filter(id=parent_id, parent_id=None).exists():
            self.http_exception(description=MESSAGE_PARENT_IS_NOT_EXISTED)

        template_group = TemplateGroup.objects.create(
            code=code,
            name=name,
            slug=slug,
            active_flag=active_flag,
            parent_id=parent_id,
            created_by=self.user.name,
            updated_by=self.user.name
        )

        return self.response_success({
            "id": template_group.id,
            "created_by": template_group.created_by,
            "created_at": template_group.created_at,
        }, status_code=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id='Template-Group-List',
        summary='List',
        tags=["Template Group"],
        description='List Template Group',
        parameters=PARAMETER_LIST_SEARCH_TEMPLATE_GROUP,
        responses={
            status.HTTP_200_OK: TemplateGroupListResponseSuccessSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_TEMPLATE_GROUP_SUCCESS,
        ]
    )
    def list(self, request):
        template_groups = TemplateGroup.objects.all().order_by('id')

        # Search
        serializer = TemplateGroupListSearchRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data['code']
        if code is not None:
            template_groups = template_groups.filter(code__icontains=code)

        name = serializer.validated_data['name']
        if name is not None:
            template_groups = template_groups.filter(name__icontains=name)

        active_flag = serializer.validated_data['active_flag']
        if active_flag is not None:
            template_groups = template_groups.filter(
                active_flag=active_flag)

        # Kiểm tra parent có tồn tại hay không, nếu không raise lỗi
        parent_id = serializer.validated_data['parent_id']
        if parent_id is not None and not TemplateGroup.objects.filter(id=parent_id, parent_id=None).exists():
            self.http_exception(description=MESSAGE_PARENT_IS_NOT_EXISTED)

        template_groups = template_groups.annotate(
            parent_name=F('parent_id__name')
        )

        # Paginator
        self.paginate(template_groups.values())

        response = TemplateGroupListItemResponseSerializer(
            self.paging_list, many=True)
        return self.response_paging(response.data)

    @extend_schema(
        operation_id='Template-Group-Detail',
        summary='Detail',
        tags=["Template Group"],
        description='Detail Template Group',
        request=TemplateGroupDetailRequestSerializer,
        responses={
            status.HTTP_200_OK: TemplateGroupDetailResponseSuccessSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_DETAIL_TEMPLATE_GROUP_SUCCESS,
        ]
    )
    def detail_template_group(self, request, template_group_id):

        template_group = self.get_model_object_by_id(
            id=template_group_id, model=TemplateGroup)

        return self.response_success({
            'id': template_group.id,
            'code': template_group.code,
            'parent_id': template_group.parent_id,
            'name': template_group.name,
            'slug': template_group.slug,
            'active_flag': template_group.active_flag,
        })

    @extend_schema(
        operation_id='Template-Group-Delete',
        summary='Delete',
        tags=["Template Group"],
        description='Delete an Template Group',
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def delete(self, request, template_group_id):
        template_group = self.get_model_object_by_id(
            id=template_group_id, model=TemplateGroup)

        # Kiểm tra Template Folder có sử dụng Template Group hay không
        if TemplateFolder.objects.filter(template_group=template_group).exists():
            return self.http_exception("Template Group is used in Template Folder")

        template_group.delete()

        return self.response_success(None, status_code=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        operation_id="Template-Group-Update",
        summary="Update",
        tags=["Template Group"],
        description="Update Template Group",
        request=TemplateGroupRequestSerializer,
        responses={
            status.HTTP_200_OK: TemplateGroupUpdateResponseSuccessSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_UPDATE_TEMPLATE_GROUP_SUCCESS],
    )
    def update(self, request, template_group_id):

        serializer = TemplateGroupRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        template_group = self.get_model_object_by_id(
            id=template_group_id, model=TemplateGroup)

        code = serializer.validated_data['code']
        # Kiểm tra code có tồn tại hay không
        # Nếu template group tồn tại và không phải là chính nó
        if code != template_group.code and TemplateGroup.objects.filter(code=code).exists():
            self.http_exception(description=MESSAGE_CODE_IS_EXISTED)

        name = serializer.validated_data['name']

        slug = serializer.validated_data['slug']
        # Kiểm tra slug có tồn tại hay không
        if slug != template_group.slug and TemplateGroup.objects.filter(slug=slug).exists():
            self.http_exception(description=MESSAGE_SLUG_IS_EXISTED)

        active_flag = serializer.validated_data['active_flag']

        # Kiểm tra parent có tồn tại hay không, nếu không raise lỗi
        parent_id = serializer.validated_data['parent_id']
        if parent_id != template_group.parent_id and parent_id is not None \
                and not TemplateGroup.objects.filter(id=parent_id, parent_id=None).exists():
            self.http_exception(description=MESSAGE_PARENT_IS_NOT_EXISTED)

        # Update Template Group
        template_group.code = code
        template_group.name = name
        template_group.slug = slug
        template_group.active_flag = active_flag
        template_group.parent_id = parent_id
        template_group.updated_by = self.user.name

        # Save
        template_group.save()

        return self.response_success(
            {
                "id": template_group_id,
                "update_by": self.user.name,
                "update_at": template_group.updated_at,
            },
            status_code=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id='Template-Group-List-Menu',
        summary='List Menu',
        tags=["Template Group"],
        description='List Menu Template Group',
        parameters=PARAMETER_LIST_MENU_TEMPLATE_GROUP,
        responses={
            status.HTTP_200_OK: TemplateGroupListMenuResponseSuccessSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_MENU_TEMPLATE_GROUP_SUCCESS,
        ]
    )
    def list_menu(self, request):
        serializer = TemplateGroupMenuRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # Nếu flag = True lấy danh sách các Menu Cha
        only_parent_menu_flag = serializer.validated_data['only_parent_menu_flag']
        if only_parent_menu_flag is True:
            '''Chỉ lấy tất cả Menu cha'''

            template_group_parents = TemplateGroup.objects.filter(parent_id=None).order_by('id').values('id', 'name')
            for template_group_parent in template_group_parents:
                template_group_parent['items'] = []

            return self.response_success(template_group_parents)

        # Nếu flag = False lấy tất cả
        template_groups = TemplateGroup.objects.all().values('id', 'parent_id', 'name').order_by('id')

        parent_list = []
        child_list = []
        items = []

        # Tách cha, con
        for template_group in template_groups:
            # Nếu Template Group cấp cao nhất <=> parent_id is Null
            if template_group['parent_id'] is None:
                parent_list.append({
                    'id': template_group['id'],
                    'name': template_group['name'],
                    'items': items
                })
            # Ngược lại là list con
            else:
                child_list.append({
                    'parent_id': template_group['parent_id'],
                    'id': template_group['id'],
                    'name': template_group['name']
                })

        for i, parent in enumerate(parent_list):
            items = []
            for child in child_list:
                # Nếu child là con của parent
                if parent['id'] == child['parent_id']:
                    items.append({
                        'id': child['id'],
                        'name': child['name'],
                    })
                    parent_list[i].update({
                        'items': items
                    })

        return self.response_success(parent_list)

    @extend_schema(
        operation_id='Template-group-check-code',
        summary='Check exist code or slug',
        tags=["Template Group"],
        description='Dùng để kiểm tra code hoặc slug có tồn tại hay chưa.'
                    'Lưu ý: CHỈ TRUYỀN LÊN 1 trong 2: `code` HOẶC `slug`',
        parameters=PARAMETER_REQUEST_CHECK_CODE_OR_SLUG_TEMPLATE_GROUP,
        responses={
            status.HTTP_200_OK: TemplateGroupCheckExistCodeResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def check_exist(self, request):
        serializer = TemplateGroupCheckExistCodeRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        is_exist = False

        code = serializer.validated_data['code']
        if code is not None:
            is_exist = TemplateGroup.objects.filter(code=code).exists()

        slug = serializer.validated_data['slug']
        if slug is not None:
            is_exist = TemplateGroup.objects.filter(slug=slug).exists()

        return self.response_success({
            "is_exist": is_exist
        }, status_code=status.HTTP_200_OK)
