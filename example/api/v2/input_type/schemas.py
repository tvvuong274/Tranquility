from drf_spectacular.utils import OpenApiExample


EXAMPLE_RESPONSE_LIST_INPUT_TYPE_SUCCESS = OpenApiExample(
    name='List all input types',
    summary='1',
    description='Constant nên id luôn cố định cho các input type khác nhau',
    value=[
        {
            "id": 1,
            "name": "Ô nhập",
            "total_used": 0
        },
        {
            "id": 2,
            "name": "Một lựa chọn",
            "total_used": 0
        },
        {
            "id": 3,
            "name": "Nhiều lựa chọn",
            "total_used": 0
        },
        {
            "id": 4,
            "name": "Ngày",
            "total_used": 0
        },
        {
            "id": 5,
            "name": "Giờ",
            "total_used": 0
        },
        {
            "id": 6,
            "name": "Ngày & Giờ",
            "total_used": 0
        },
        {
            "id": 7,
            "name": "Phương tiện",
            "total_used": 0
        },
        {
            "id": 8,
            "name": "Tập tin",
            "total_used": 0
        },
        {
            "id": 9,
            "name": "Đánh giá",
            "total_used": 0
        },
        {
            "id": 10,
            "name": "Phạm vi",
            "total_used": 0
        },
        {
            "id": 11,
            "name": "Câu hỏi Đúng/Sai",
            "total_used": 0
        },
        {
            "id": 12,
            "name": "Chuyển đổi Bật/Tắt",
            "total_used": 0
        },
        {
            "id": 13,
            "name": "Chữ ký",
            "total_used": 0
        },
        {
            "id": 14,
            "name": "Nhóm",
            "total_used": 0
        }
    ],
    # status_codes=["200"],
    # request_only=True,  # signal that example only applies to requests
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_LIST_FORMAT_OF_AN_INPUT_TYPE_SUCCESS = OpenApiExample(
    name='List all formats of an input type',
    summary='1',
    description='Constant nên id luôn cố định cho các input type format khác nhau',
    value=[
        {
            "id": 1,
            "description": "Ô nhập định dạng tự do",
            "conditions": [
                {
                    "checked_flag": None,
                    "name": "Giới hạn ký tự",
                    "action": "limit_character",
                    "type": "text",
                    "value": "255"
                },
                {
                    "checked_flag": None,
                    "name": "Cho phép nhập văn bản",
                    "type": "radio",
                    "action": None,
                    "value": [
                        {
                            "checked_flag": False,
                            "name": "Chỉ văn bản",
                            "action": "enter_only_alpha",
                            "type": None,
                            "value": None
                        },
                        {
                            "checked_flag": False,
                            "name": "Chỉ số",
                            "action": "enter_only_number",
                            "type": None,
                            "value": False
                        },
                        {
                            "checked_flag": True,
                            "name": "Bao gồm các kí tự đặc biệt",
                            "action": "enter_text",
                            "type": None,
                            "value": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 2,
            "description": "Ô nhập định dạng tùy chỉnh",
            "conditions": [
                {
                    "checked_flag": None,
                    "name": "Giới hạn ký tự",
                    "action": "limit_character",
                    "type": "text",
                    "value": "255"
                },
                {
                    "checked_flag": None,
                    "name": "Cho phép nhập văn bản",
                    "type": "radio",
                    "action": None,
                    "value": [
                        {
                            "checked_flag": False,
                            "name": "Chỉ văn bản",
                            "action": "enter_only_alpha",
                            "type": None,
                            "value": None
                        },
                        {
                            "checked_flag": False,
                            "name": "Chỉ số",
                            "action": "enter_only_number",
                            "type": None,
                            "value": False
                        },
                        {
                            "checked_flag": True,
                            "name": "Bao gồm các kí tự đặc biệt",
                            "action": "enter_text",
                            "type": None,
                            "value": None
                        }
                    ]
                }
            ]
        }
    ],
    # status_codes=["200"],
    # request_only=True,  # signal that example only applies to requests
    response_only=True  # signal that example only applies to responses
)

EXAMPLE_RESPONSE_JSON_CONDITION_OF_AN_INPUT_TYPE_FORMAT_SUCCESS = OpenApiExample(
    name='Json condition of an input type format',
    summary='Invalid password',
    description='',
    value=[
        {
            "checked_flag": None,
            "name": "Giới hạn ký tự",
            "action": "limit_character",
            "type": "text",
            "value": "255"
        },
        {
            "checked_flag": None,
            "name": "Cho phép nhập văn bản",
            "type": "radio",
            "action": None,
            "value": [
                {
                    "checked_flag": False,
                    "name": "Chỉ văn bản",
                    "action": "enter_only_alpha",
                    "type": None,
                    "value": None
                },
                {
                    "checked_flag": False,
                    "name": "Chỉ số",
                    "action": "enter_only_number",
                    "type": None,
                    "value": False
                },
                {
                    "checked_flag": True,
                    "name": "Bao gồm các kí tự đặc biệt",
                    "action": "enter_text",
                    "type": None,
                    "value": None
                }
            ]
        }
    ],
    response_only=True
)
