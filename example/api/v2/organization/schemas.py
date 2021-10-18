from drf_spectacular.utils import OpenApiExample

EXAMPLE_RESPONSE_LIST_BLOCK_SUCCESS = OpenApiExample(
    name='Block List',
    description='',
    value=[
        {
            "id": 1,
            "name": "block1"
        },
        {
            "id": 2,
            "name": "block2"
        }
    ],
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_LIST_DEPARTMENT_SUCCESS = OpenApiExample(
    name='Department List',
    description='',
    value=[
        {
            "id": 1,
            "name": "department1"
        },
        {
            "id": 2,
            "name": "department2"
        }
    ],
    response_only=True  # signal that example only applies to responses
)
