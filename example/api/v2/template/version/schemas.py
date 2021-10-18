from drf_spectacular.utils import OpenApiExample


EXAMPLE_RESPONSE_LIST_VERSION_SUCCESS = OpenApiExample(
    name='List version',
    summary='1',
    description='Version',
    value=[
        {
            "id": 1,
            "code": "456sdf",
            "name": "BM2",
            "version": 1.0,
            "start_date": "2021-08-18 08:48:29",
            "end_date": "2021-11-17 08:48:33",
            "updated_by": "admin"
        }
    ],
    response_only=True  # signal that example only applies to responses
)
