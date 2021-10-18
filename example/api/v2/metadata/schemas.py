from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


EXAMPLE_RESPONSE_CREATE_METADATA_SUCCESS = OpenApiExample(
    name='Create success',
    summary='1',
    description='Create',
    value={
        "id": 1,
        "name": "string",
        "created_by": "admin"
    },
    response_only=True
)
EXAMPLE_RESPONSE_UPDATE_METADATA_SUCCESS = OpenApiExample(
    name='Update success',
    summary='1',
    description='Update',
    value={
        "id": 1,
        "created_by": "admin",
        "updated_by": "admin"
    },
    response_only=True
)

EXAMPLE_RESPONSE_DETAIL_METADATA_SUCCESS = OpenApiExample(
    name='Detail a Metadata',
    description='',
    value={
        "id": 1,
        "name": "tên metadata",
        "code": "code meta...",
        "active_flag": True,
        "output_edit_flag": True,
        "list_c_system_type": [1, 2, 3],
        "input_type_format_id": 1,
        "input_condition_json": {},
        "metadata_group_id": 1,
        "note": "Nhập ghi chú",
       
    },
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_LIST_METADATA_GROUP_SUCCESS = OpenApiExample(
    name='Metadata group',
    description='',
    value=[
        {
            "id": 1,
            "name": "Thông Tin Cá Nhân"
        },
        {
            "id": 21,
            "name": "Thông Tin Tín Dụng"
        },
        {
            "id": 22,
            "name": "Thông Tin Tài Sản Đảm Bảo"
        }
    ],
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_LIST_METADATA_SUCCESS = OpenApiExample(
    name='List metadata',
    summary='1',
    description='Constant nên id luôn cố định cho các input type khác nhau',
    value={
        "items": [
            {
                "id": 3,
                "name": "BC_chinhanh",
                "code": "BC_chinhanh",
                "input_type_name": "Ô nhập",
                "number_template": 0,
                "list_c_system_type": [
                    2
                ],
                "list_system_type_name": [
                    "LOS"
                ],
                "metadata_group_id": 1,
                "metadata_group_name": "test",
                "active_flag": True
            },
        ],
        "total_page": 1,
        "total_record": 5,
        "page": 1
    },
    response_only=True  # signal that example only applies to responses
)

PARAMETER_REQUEST_LIST_METADATA = [
    OpenApiParameter(
        name='input_type_id',
        type=OpenApiTypes.INT,
        description='Lọc theo `Loại nhập liệu`',
        examples=[
            OpenApiExample(
                'Ô nhập',
                description='Ô nhập',
                value='1'
            ),
            OpenApiExample(
                'Một lựa chọn',
                description='Một lựa chọn',
                value='2'
            ),
            OpenApiExample(
                'Nhiều lựa chọn',
                description='Nhiều lựa chọn',
                value='3'
            ),
            OpenApiExample(
                'Ngày',
                description='Ngày',
                value='4'
            ),
            OpenApiExample(
                'Giờ',
                description='Giờ',
                value='5'
            ),
            OpenApiExample(
                'Ngày & Giờ',
                description='Ngày & Giờ',
                value='6'
            ),
            OpenApiExample(
                'Phương tiện',
                description='Phương tiện',
                value='7'
            ),
            OpenApiExample(
                'Tập tin',
                description='Tập tin',
                value='8'
            ),
            OpenApiExample(
                'Đánh giá',
                description='Đánh giá',
                value='9'
            ),
            OpenApiExample(
                'Phạm vi',
                description='Phạm vi',
                value='10'
            ),
            OpenApiExample(
                'Câu hỏi Đúng/Sai',
                description='Câu hỏi Đúng/Sai',
                value='11'
            ),
            OpenApiExample(
                'Chuyển đổi Bật/Tắt',
                description='Chuyển đổi Bật/Tắt',
                value='12'
            ),
            OpenApiExample(
                'Chữ ký',
                description='Chữ ký',
                value='13'
            ),
            OpenApiExample(
                'Nhóm',
                description='Nhóm',
                value='14'
            )
        ]
    ),
    OpenApiParameter(
        name='name',
        description='Lọc theo `Tên metadata`'
    ),
    OpenApiParameter(
        name='active_flag',
        type=OpenApiTypes.BOOL,
        description='Lọc theo `Trạng thái`'
    ),
    OpenApiParameter(
        name='list_c_system_type',
        type=OpenApiTypes.ANY,
        description='Lọc theo `Hệ thống`',
        examples=[
            OpenApiExample(
                'CRM',
                description='CRM',
                value='[1]'
            ),
            OpenApiExample(
                'LOS',
                description='LOS',
                value='[2]'
            ),
            OpenApiExample(
                'HRM',
                description='HRM',
                value='[3]'
            ),
            OpenApiExample(
                'All',
                description='Cả 3 hệ thống CRM, LOS và HRM',
                value='[1, 2, 3]'
            )
        ],
    ),
    OpenApiParameter(
        name='page',
        description='Page number`'
    ),
    OpenApiParameter(
        name='limit',
        description='Limit number rows`'
    ),
]

PARAMETER_REQUEST_CHECK_CODE_METADATA = [
    OpenApiParameter(
        name='code',
        description='`code` need to check exist',
        required=True
    )
]
