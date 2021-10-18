from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiTypes

# List
PARAMETER_LIST_SEARCH_TEMPLATE_GROUP = [
    OpenApiParameter(name="code", type=OpenApiTypes.STR,
                     description="Lọc theo `Code`"),
    OpenApiParameter(name="parent_id", type=OpenApiTypes.INT,
                     description="Lọc theo `Menu Cha`"),
    OpenApiParameter(name="name", type=OpenApiTypes.STR,
                     description="Lọc theo `Tên Menu`"),
    OpenApiParameter(name="active_flag", type=OpenApiTypes.BOOL,
                     description="Lọc theo `Trạng thái`"),
    OpenApiParameter(name="limit", type=OpenApiTypes.INT,
                     description="Giới hạn `Số dòng`"),
    OpenApiParameter(name="page", type=OpenApiTypes.INT,
                     description="`Số trang`"),
]

EXAMPLE_RESPONSE_LIST_TEMPLATE_GROUP_SUCCESS = OpenApiExample(
    name="List Template Group Success",
    description="List Template Group Success",
    value={
        "items": [
            {
                "id": 1,
                "code": "VANHANH",
                "name": "VẬN HÀNH",
                "slug": "van-hanh",
                "active_flag": True,
                "parent_id": None,
                "parent_name": ""
            },
            {
                "id": 12,
                "code": "MAURIENG4",
                "name": "MẪU RIÊNG",
                "slug": "mau-rieng-4",
                "active_flag": True,
                "parent_id": 4,
                "parent_name": "KHỐI KHDN"
            }
        ],
        "total_page": 1,
        "total_record": 12,
        "page": 1
    },
    status_codes=["200"],
    response_only=True,  # signal that example only applies to responses
)

# Detail
EXAMPLE_RESPONSE_DETAIL_TEMPLATE_GROUP_SUCCESS = OpenApiExample(
    name="Detail Template Group Success",
    description="Detail Template Group Success",
    value={
        "id": 1,
        "code": "VANHANH",
        "parent_id": None,
        "name": "VẬN HÀNH",
        "slug": "van-hanh",
        "active_flag": True
    },
    status_codes=["200"],
    response_only=True,  # signal that example only applies to responses
)

# Update
EXAMPLE_RESPONSE_UPDATE_TEMPLATE_GROUP_SUCCESS = OpenApiExample(
    name="Update Template Group Success",
    description="Update Template Group Success",
    value={
        "id": 8,
        "update_by": "ADMIN",
        "update_at": "2021-08-18 12:40:16"
    },
    status_codes=["200"],
    response_only=True,  # signal that example only applies to responses
)

# Menu
PARAMETER_LIST_MENU_TEMPLATE_GROUP = [
    OpenApiParameter(
        name="only_parent_menu_flag", type=OpenApiTypes.BOOL,
        description="`only_parent_menu_flag`=True khi chỉ cần danh sách Menu Cha"
    )
]

EXAMPLE_RESPONSE_LIST_MENU_TEMPLATE_GROUP_SUCCESS = OpenApiExample(
    name="List Menu Template Group Success",
    description="List Menu Template Group Success",
    value=[
        {
            "id": 1,
            "name": "VẬN HÀNH",
            "items": [
                {
                    "id": 5,
                    "name": "MẪU CHUNG"
                },
                {
                    "id": 6,
                    "name": "MẪU RIÊNG"
                }
            ]
        },
        {
            "id": 2,
            "name": "TÍN DỤNG",
            "items": [
                {
                    "id": 7,
                    "name": "MẪU CHUNG"
                },
                {
                    "id": 8,
                    "name": "MẪU RIÊNG"
                }
            ]
        },
        {
            "id": 3,
            "name": "KHỐI KHCN",
            "items": [
                {
                    "id": 9,
                    "name": "MẪU CHUNG"
                },
                {
                    "id": 10,
                    "name": "MẪU RIÊNG"
                }
            ]
        },
        {
            "id": 4,
            "name": "KHỐI KHDN",
            "items": [
                {
                    "id": 11,
                    "name": "MẪU CHUNG"
                },
                {
                    "id": 12,
                    "name": "MẪU RIÊNG"
                }
            ]
        }
    ],
    status_codes=["200"],
    response_only=True,  # signal that example only applies to responses
)

PARAMETER_REQUEST_CHECK_CODE_OR_SLUG_TEMPLATE_GROUP = [
    OpenApiParameter(
        name='code',
        description='`code` need to check exist. Truyền code thì không truyền slug',
        required=True
    ),
    OpenApiParameter(
        name='slug',
        description='`slug` need to check exist. Truyền slug thì không truyền code',
        required=True
    )
]
