from django.utils import tree
from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_CREATED_SUCCESS = OpenApiExample(
    name="Create success",
    summary="1",
    description="Create",
    value={
        "id": 32,
        "created_by": "ADMIN",
    },
    response_only=True,
)

EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_UPDATED_SUCCESS = OpenApiExample(
    name="Update success",
    summary="1",
    description="Update",
    value={
        "id": 32,
        "updated_by": "ADMIN",
    },
    response_only=True,
)

EXAMPLE_RESPONSE_CREATE_METADATA_COMMENT_LIST_SUCCESS = OpenApiExample(
    name="List success",
    summary="1",
    description="List",
    value=[
        {
            "userid": 21,
            "username": "admin",
            "name": "ADMIN",
            "avatar_url": "",
            "content": "<a href='#'>This is comment of metadata</a>",
            "log_flag": False,
            "created_at": "2021-08-18 13:36:51",
            "updated_at": "2021-08-18 13:36:51",
        }
    ],
    response_only=True,
)
