from drf_spectacular.utils import OpenApiExample, OpenApiParameter

EXAMPLE_RESPONSE_CREATE_DATA_SOURCE_API = OpenApiExample(
    name='Create success',
    summary='1',
    description='create',
    value={
        'id': 1,
        'name': 'API khách hàng',
        'template_id': '1',
        'created_by': 'admin'
    },
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_REQUEST_BEARER_TOKEN_CREATE_UPDATE_DATA_SOURCE_API = OpenApiExample(
    name='Bearer token',
    summary='2',
    description='Bearer token',
    value=
    {
        "name": "abvcfff",
        "c_method_type": 1,
        "c_auth_type": 2,
        "auth_json": {
            "token": "123"
        },
        "url": "https://stackoverflow.com/",
        "header_list":
            [
                {
                    "key": "Content-Type",
                    "value": "application/json",
                    "description": "mo ta"
                },
                {
                    "key": "Content-Type",
                    "value": "application/json",
                    "description": "mo ta"
                }
            ],
        "body_json": {
            "customer_id": 123
        }
    },
    request_only=True
)

EXAMPLE_REQUEST_BASIC_AUTH_CREATE_UPDATE_DATA_SOURCE_API = OpenApiExample(
    name='Basic auth',
    summary='1',
    description='Basic auth',
    value=
    {
        "name": "abvcfff",
        "c_method_type": 1,
        "c_auth_type": 2,
        "auth_json": {
            "username": "abc",
            "password": "abc"
        },
        "url": "https://stackoverflow.com/",
        "header_list":
            [
                {
                    "key": "Content-Type",
                    "value": "application/json",
                    "description": "mo ta"
                },
                {
                    "key": "Content-Type",
                    "value": "application/json",
                    "description": "mo ta"
                }
            ],
        "body_json": {
            "customer_id": 123
        }
    },
    request_only=True
)

EXAMPLE_RESPONSE_UPDATE_DATA_SOURCE_API = OpenApiExample(
    name='Update success',
    summary='1',
    description='update',
    value={
        'id': 1,
        'name': 'API khách hàng',
        'template_id': '1',
        'updated_by': 'admin'
    },
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_LIST_ALL_DATA_SOURCE_API_SUCCESS = OpenApiExample(
    name='List all data source api',
    summary='1',
    description='list',
    value=
    [
        {
            'id': 1,
            'name': 'API khách hàng',
        },
        {
            'id': 2,
            'name': 'API tài khoản',
        }

    ]
)

EXAMPLE_RESPONSE_LIST_DATA_SOURCE_API_OF_TEMPLATE_SUCCESS = OpenApiExample(
    name='List data source api of template',
    summary='1',
    description='list',
    value=
    [
        {
            'id': 1,
            'data_source_api_id': 1,
            'data_source_api_name': 'API khách hàng'
        },
        {
            'id': 2,
            'data_source_api_id': 2,
            'data_source_api_name': 'API thu nhập'
        }
    ]
)

EXAMPLE_RESPONSE_DETAIL_DATA_SOURCE_API = OpenApiExample(
    name='detail data source api',
    summary='1',
    description='Detail of data source api',
    value={
        'id': 1,
        'name': 'API khách hàng',
        'c_method_type': 1,
        "url": "https://stackoverflow.com/?id=123",
        'c_auth_type': 2,
        'auth_json':
            {
                "token": "askljdfaskljdfaskljs"
            },
        'header_list':
            {
                "key": "Content-Type",
                "value": "application/json",
                "description": "mo ta"
            },
        'body_json':
            {
                "customer_id": 123
            }
    }
)

EXAMPLE_RESPONSE_COPY_DATA_SOURCE_API = OpenApiExample(
    name='Copy success',
    summary='1',
    description='copy',
    value={
        'id': 1,
        'name': 'API khách hàng',
        'template_id': '1',
        'created_by': 'admin',
        'updated_by': 'admin'
    },
    response_only=True  # signal that example only applies to responses
)

PARAMETER_REQUEST_DATA_SOURCE_API = [
    OpenApiParameter(
        name='name',
        description='Lọc theo tên data source api'
    )
]
