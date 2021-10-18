from django.db.models import Q

from api.base.base_views import BaseAPIView
from drf_spectacular.utils import extend_schema
from rest_framework import status
from api.base.serializers import ExceptionResponseSerializer

from db_models.template.folder.models import TemplateFolder
from db_models.template.group.models import TemplateGroup
from db_models.template.models import Template
from api.v2.template_group.template_folder.serializers import (
    FolderCreateRequestSerializer,
    FolderCreateSuccessResponseSerializer,
    FolderUpdateRequestSerializer,
    FolderUpdateSuccessResponseSerializer,
    TemplateFolderListResponseSuccessSerializer,
    TemplateFolderMenuRequestSerializer,
    TemplateFolderListMenuResponseSuccessSerializer,
    TemplateFolderCheckExistSlugRequestSerializer,
    TemplateFolderCheckExistSlugResponseSerializer
)
from api.v2.template_group.template_folder.schemas import (
    EXAMPLE_RESPONSE_LIST_TEMPLATE_FOLDER_SUCCESS,
    EXAMPLE_RESPONSE_CREATE_TEMPLATE_FOLDER_SUCCESS,
    EXAMPLE_RESPONSE_UPDATE_TEMPLATE_FOLDER_SUCCESS,
    PARAMETER_REQUEST_LIST_TEMPLATE_FOLDER,
    EXAMPLE_RESPONSE_LIST_MENU_TEMPLATE_FOLDER_SUCCESS,
    PARAMETER_REQUEST_CHECK_SLUG_TEMPLATE_FOLDER
)


class FolderViews(BaseAPIView):
    @staticmethod
    def _get_parent_folders(template_group_id, parent_id=None):
        folders = TemplateFolder.objects.filter(
            template_group=template_group_id
        ).values(
            'id',
            'name',
            'slug',
            'updated_by',
            'updated_at',
            'parent_id'
        ).order_by('id')

        if parent_id is not None:
            folders = folders.filter(Q(parent_id=parent_id) | Q(id=parent_id))

        parent_folders = []
        child_folders = []

        for folder in folders:
            if folder['parent_id'] is None:
                parent_folders.append(folder)
            else:
                child_folders.append(folder)

        for index, parent_folder in enumerate(parent_folders):
            parent_folders[index]['child'] = []
            for child_folder in child_folders:
                # Nếu child folder là con của parent folder
                if child_folder['parent_id'] == parent_folder['id']:
                    parent_folders[index]['child'].append(child_folder)

        return parent_folders

    @extend_schema(
        operation_id='Template-Folder-List-Menu',
        summary='List Menu',
        tags=["Template Folder"],
        description='List Menu Template Folder',
        parameters=PARAMETER_REQUEST_LIST_TEMPLATE_FOLDER,
        responses={
            status.HTTP_200_OK: TemplateFolderListMenuResponseSuccessSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_MENU_TEMPLATE_FOLDER_SUCCESS,
        ]
    )
    def list_menu(self, request, template_group_id):
        serializer = TemplateFolderMenuRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        parent_id = serializer.validated_data.get('parent_id')
        parent_folders = self._get_parent_folders(template_group_id=template_group_id, parent_id=parent_id)

        serializer_response = TemplateFolderListMenuResponseSuccessSerializer(parent_folders, many=True)

        return self.response_success(serializer_response.data)

    @extend_schema(
        operation_id='Template-Folder-List',
        summary='List',
        tags=["Template Folder"],
        description='List Template Folder',
        responses={
            status.HTTP_200_OK: TemplateFolderListResponseSuccessSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[
            EXAMPLE_RESPONSE_LIST_TEMPLATE_FOLDER_SUCCESS,
        ]
    )
    def list(self, request, template_group_id):
        parent_folders = self._get_parent_folders(template_group_id=template_group_id)

        serializer_response = TemplateFolderListResponseSuccessSerializer(parent_folders, many=True)

        return self.response_success(serializer_response.data)

    @extend_schema(
        operation_id='Template-Folder-Create',
        summary='Create',
        tags=["Template Folder"],
        description='Create Template Folder',
        request=FolderCreateRequestSerializer,
        responses={
            status.HTTP_201_CREATED: FolderCreateSuccessResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer
        },
        examples=[
            EXAMPLE_RESPONSE_CREATE_TEMPLATE_FOLDER_SUCCESS,
        ]
    )
    def create(self, request, template_group_id):
        serializer = FolderCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        template_group = self.get_model_object_by_id(
            id=template_group_id,
            model=TemplateGroup
        )

        slug = serializer.validated_data['slug']
        if TemplateFolder.objects.filter(slug__exact=slug).exists():
            return self.http_exception(description='slug already exists')

        parent_id = serializer.validated_data['parent_id']
        if parent_id is not None:
            if not TemplateFolder.objects.filter(id=parent_id, parent_id=None).exists():
                return self.http_exception(description='parent_id is not exist')

        folder = TemplateFolder.objects.create(
            name=serializer.validated_data['name'],
            slug=slug,
            parent_id=parent_id,
            template_group=template_group,
            created_by=self.user.name,
            updated_by=self.user.name
        )

        return self.response_success({
            'id': folder.id,
            'name': folder.name,
            'created_by': folder.created_by
        }, status_code=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id='Template-Folder-Update',
        summary='Update',
        tags=["Template Folder"],
        description='Update Template Folder',
        request=FolderUpdateRequestSerializer,
        responses={
            status.HTTP_200_OK: FolderUpdateSuccessResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer
        },
        examples=[
            EXAMPLE_RESPONSE_UPDATE_TEMPLATE_FOLDER_SUCCESS,
        ]
    )
    def update(self, request, template_group_id, folder_id):
        serializer = FolderUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.get_model_object_by_id(id=template_group_id, model=TemplateGroup)

        folder = self.get_model_object_by_id(id=folder_id, model=TemplateFolder)
        
        slug = serializer.validated_data['slug']
        if slug != folder.slug:
            if TemplateFolder.objects.filter(slug__exact=slug).exists():
                return self.http_exception(description='slug already exists')

        folder.name = serializer.validated_data['name']
        folder.slug = slug
        folder.updated_by = self.user.name

        folder.save()

        return self.response_success({
            "id": folder.id,
            "created_by": folder.created_by,
            "updated_by": folder.updated_by
        })

    @extend_schema(
        operation_id='Template-Folder-Delete',
        summary='Delete',
        tags=["Template Folder"],
        description='Delete an Folder',
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def delete(self, request, folder_id, template_group_id):
        self.get_model_object_by_id(id=template_group_id, model=TemplateGroup)

        folder = self.get_model_object_by_id(id=folder_id, model=TemplateFolder)

        # Kiểm tra ràng buộc nếu template_foldel được sử dụng thì không được xóa
        if Template.objects.filter(template_folder=folder_id).exists():
            return self.http_exception("Delete Template before delete folder")

        folder.delete()

        return self.response_success(None, status_code=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        operation_id='Template-folder-check-slug',
        summary='Check exist slug',
        tags=["Template Folder"],
        description='Template Folder check slug',
        parameters=PARAMETER_REQUEST_CHECK_SLUG_TEMPLATE_FOLDER,
        responses={
            status.HTTP_200_OK: TemplateFolderCheckExistSlugResponseSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        }
    )
    def check_exist(self, request, template_group_id):
        serializer = TemplateFolderCheckExistSlugRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        is_exist = TemplateFolder.objects.filter(template_group=template_group_id, slug=serializer.validated_data['slug']).exists()

        return self.response_success({
            "is_exist": is_exist
        }, status_code=status.HTTP_200_OK)
