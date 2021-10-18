from library.constant.template import (
    TEMPLATE_DEFAULT_SORT, 
    TEMPLATE_DEFAULT_SORT_A_TO_Z, 
    TEMPLATE_DEFAULT_SORT_Z_TO_A
)
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiTypes


# List
PARAMETER_LIST_TEMPLATE = [
    OpenApiParameter(
        name="name", type=OpenApiTypes.STR, description="Tìm kiếm theo `Tên biểu mẫu`"
    ),
    OpenApiParameter(
        name="sort",
        type=OpenApiTypes.INT,
        description="Sắp xếp",
        examples=[
            OpenApiExample(
                "A-Z", 
                description=TEMPLATE_DEFAULT_SORT[TEMPLATE_DEFAULT_SORT_A_TO_Z], 
                value=str(TEMPLATE_DEFAULT_SORT_A_TO_Z)
            ),
            OpenApiExample(
                "Z-A", 
                description=TEMPLATE_DEFAULT_SORT[TEMPLATE_DEFAULT_SORT_Z_TO_A], 
                value=str(TEMPLATE_DEFAULT_SORT_Z_TO_A)
            ),
        ],
    ),
    OpenApiParameter(name="start_date", type=OpenApiTypes.DATE,
                     description="`Ngày bắt đầu` nhỏ nhất trong list item"),
    OpenApiParameter(name="end_date", type=OpenApiTypes.DATE,
                     description="`Ngày kết thúc` lớn nhất trong list item"),
    OpenApiParameter(name="limit", type=OpenApiTypes.INT,
                     description="Giới hạn `Số dòng`"),
    OpenApiParameter(name="page", type=OpenApiTypes.INT,
                     description="`Số trang`"),
]


EXAMPLE_RESPONSE_LIST_TEMPLATE_SUCCESS = OpenApiExample(
    name="List template",
    summary="1",
    description="",
    value={
    "items": [
            {
                "id": 1,
                "name": "BM2",
                "version": 1.0,
                "start_date": "2021-08-18",
                "updated_by": "admin",
                "updated_at": "2021-08-17 08:47:46",
                "c_status": True,
                "list_system_type_name": "['CRM', 'LOS']"
            },
            {
                "id": 135,
                "name": "BM1",
                "version": 2.0,
                "start_date": "2021-08-17",
                "updated_by": "admin",
                "updated_at": "2021-08-17 22:45:47",
                "c_status": True,
                "list_system_type_name": "['CRM']"
            },
        ],
        "total_page": 1,
        "total_record": 2,
        "page": 1,
        "start_date": "2021-08-17",
        "end_date": "2021-11-17"
    },
    # status_codes=["200"],
    # request_only=True,  # signal that example only applies to requests
    response_only=True,  # signal that example only applies to responses
)

PARAMETER_REQUEST_CHECK_CODE_TEMPLATE = [
    OpenApiParameter(
        name='code',
        description='`code` need to check exist',
        required=True
    )
]
