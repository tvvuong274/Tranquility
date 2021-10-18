from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

EXAMPLE_RESPONSE_LIST_TEMPLATE_FOLDER_SUCCESS = OpenApiExample(
    name="List Template Folder Success",
    description="List Template folder Success",
    value=[
        {
            "id": 1,
            "name": "PHÂN HỆ TERM DEPOSIT1",
            "slug": "mau-chung/khcn/thong-tin-cif",
            "updated_by": "ADMIN",
            "updated_at": "2021-08-16 22:01:57",
            "child": [
                {
                    "id": 2,
                    "name": "PHÂN HỆ TERM DEPOSIT2",
                    "slug": "mau-chung/khcn/thong-tin-cif",
                    "updated_by": "ADMIN",
                    "updated_at": "2021-08-17 14:24:22"
                }
            ]
        }
    ],
    status_codes=["200"],
    response_only=True,  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_LIST_MENU_TEMPLATE_FOLDER_SUCCESS = OpenApiExample(
    name="List Template Folder Success",
    description="List Template folder Success",
    value=[
        {
            "id": 1,
            "name": "PHÂN HỆ CIF",
            "child": [
                {
                    "id": 10,
                    "name": "Mở CIF"
                },
                {
                    "id": 11,
                    "name": "Nguồn thu nhập"
                }
            ]
        },
        {
            "id": 2,
            "name": "PHÂN HỆ CASA",
            "child": []
        },
        {
            "id": 3,
            "name": "PHÂN HỆ TERM DEPOSIT",
            "child": []
        },
        {
            "id": 4,
            "name": "PHÂN HỆ TELLER - KÊNH TIỀN MẶT",
            "child": []
        },
        {
            "id": 5,
            "name": "PHÂN HỆ TELLER - KÊNH CHUYỂN KHOẢN",
            "child": []
        },
        {
            "id": 6,
            "name": "PHÂN HỆ CHUYỂN TIỀN QUỐC TẾ",
            "child": []
        }
    ],

    status_codes=["200"],
    response_only=True,  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_CREATE_TEMPLATE_FOLDER_SUCCESS = OpenApiExample(
    name='Create success',
    summary='1',
    description='Create',
    value={
        "id": 43,
        "name": "PHÂN HỆ TERM DEPOSIT2",
        "created_by": "ADMIN"
    },
    response_only=True
)

EXAMPLE_RESPONSE_UPDATE_TEMPLATE_FOLDER_SUCCESS = OpenApiExample(
    name='Create success',
    summary='1',
    description='Create',
    value={
        "id": 1,
        "created_by": "ADMIN",
        "updated_by": "ADMIN"
    },
    response_only=True
)

PARAMETER_REQUEST_LIST_TEMPLATE_FOLDER = [
    OpenApiParameter(
        name='parent_id',
        type=OpenApiTypes.INT,
        description='Chỉ filter theo parent_id (menu cha bên ngoài)',
        examples=[
            OpenApiExample(
                'PHÂN HỆ CIF',
                description='PHÂN HỆ CIF',
                value='1'
            ),
            OpenApiExample(
                'PHÂN HỆ CASA',
                description='PHÂN HỆ CASA',
                value='2'
            ),
            OpenApiExample(
                'PHÂN HỆ TERM DEPOSIT',
                description='PHÂN HỆ TERM DEPOSIT',
                value='3'
            ),
            OpenApiExample(
                'PHÂN HỆ TELLER - KÊNH TIỀN MẶT',
                description='PHÂN HỆ TELLER - KÊNH TIỀN MẶT',
                value='4'
            ),
            OpenApiExample(
                'PHÂN HỆ TELLER - KÊNH CHUYỂN KHOẢN',
                description='PHÂN HỆ TELLER - KÊNH CHUYỂN KHOẢN',
                value='5'
            ),
            OpenApiExample(
                '',
                description='',
                value='...'
            )
        ],
    )
]

PARAMETER_REQUEST_CHECK_SLUG_TEMPLATE_FOLDER = [
    OpenApiParameter(
        name='slug',
        description='`slug` need to check exist',
        required=True
    )
]
