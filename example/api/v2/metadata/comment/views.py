from django.db.models import F
from rest_framework import status

from drf_spectacular.utils import extend_schema
from api.base.serializers import ExceptionResponseSerializer
from api.base.base_views import BaseAPIView

from db_models.user.models import User
from db_models.metadata.models import Metadata
from db_models.metadata.comment.models import MetadataComment
from .schemas import (
    EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_CREATED_SUCCESS,
    EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_UPDATED_SUCCESS,
    EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_LIST_SUCCESS,
)

from .serializers import (
    MetadataCommentCreateResponeSerializer,
    MetadataCommentCreateUpdateRequestSerializer,
    MetadataCommentResponseListSerializer,
    MetadataCommentUpdateResponeSerializer,
)


class MetadataCommentView(BaseAPIView):
    @extend_schema(
        operation_id="create",
        summary="Create",
        tags=["MetadataComment"],
        request=MetadataCommentCreateUpdateRequestSerializer,
        description="Create MetadataComment",
        responses={
            status.HTTP_201_CREATED: MetadataCommentCreateResponeSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_CREATED_SUCCESS],
    )
    def create(self, request, metadata_id):
        """
        [API] Create Metadata-Comment.
        """
        metadata = self.get_model_object_by_id(metadata_id, Metadata)

        serializer = MetadataCommentCreateUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        metadata_comment = MetadataComment.objects.create(
            metadata=metadata,
            user=self.user,
            log_flag=False,
            content=serializer.validated_data["content"],
            created_by=self.user.name,
            updated_by=self.user.name,
        )

        response = MetadataCommentCreateResponeSerializer(
            {
                "id": metadata_comment.id,
                "created_by": self.user.name,
            }
        )
        return self.response_success(response.data, status_code=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id="update",
        summary="Update",
        tags=["MetadataComment"],
        request=MetadataCommentCreateUpdateRequestSerializer,
        description="Update MetadataComment",
        responses={
            status.HTTP_200_OK: MetadataCommentUpdateResponeSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_UPDATED_SUCCESS],
    )
    def update(self, request, metadata_id, metadata_comment_id):
        """
        [API] Update Metadata-Comment.
        """
        serializer = MetadataCommentCreateUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        content = serializer.validated_data["content"]
        if content == "":
            return self.http_exception(description="Content should not be empty")

        metadata_comment = self.get_model_object_by_id(metadata_comment_id, MetadataComment)
        metadata_comment.content = content
        metadata_comment.save()

        response = MetadataCommentUpdateResponeSerializer(
            {
                "id": metadata_comment.id,
                "updated_by": self.user.name,
            }
        )
        return self.response_success(response.data, status_code=status.HTTP_200_OK)

    @extend_schema(
        operation_id="list-comments",
        summary="List",
        tags=["MetadataComment"],
        description="List comments of Metadata",
        responses={
            status.HTTP_200_OK: MetadataCommentResponseListSerializer,
            status.HTTP_401_UNAUTHORIZED: ExceptionResponseSerializer,
            status.HTTP_400_BAD_REQUEST: ExceptionResponseSerializer,
        },
        examples=[EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_LIST_SUCCESS],
    )
    def list(self, request, metadata_id):
        """
        [API] List Metadata-Comment
        """
        metadata = self.get_model_object_by_id(metadata_id, Metadata)
        comments = (
            MetadataComment.objects.filter(
                metadata=metadata,
            )
            .annotate(
                userid=F("user__id"),
                username=F("user__username"),
                name=F("user__name"),
                avatar_url=F("user__avatar_url"),
            )
            .order_by("id")
            .values(
                "userid",
                "username",
                "name",
                "avatar_url",
                "content",
                "log_flag",
                "created_at",
                "updated_at",
            )
        )
        response = MetadataCommentResponseListSerializer(comments, many=True)

        return self.response_success(
            response.data,
            status_code=status.HTTP_204_NO_CONTENT,
        )
