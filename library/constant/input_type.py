from django.utils.translation import ugettext_lazy as _

from library.constant.file_extension import FILE_EXTENSION_PNG, FILE_EXTENSION_SVG, FILE_EXTENSION_JPG, \
    FILE_EXTENSION_HEIC, FILE_EXTENSION_MP4, FILE_EXTENSION_WMV, FILE_EXTENSION_F4V, FILE_EXTENSION_AVI, \
    FILE_EXTENSION_WEBM, FILE_EXTENSION_MP3, FILE_EXTENSION_DOCX, FILE_EXTENSION_DOC, FILE_EXTENSION_XLS, \
    FILE_EXTENSION_PPTX, FILE_EXTENSION_PDF, FILE_EXTENSION_TXT, FILE_EXTENSION_ZIP, FILE_EXTENSION_RAR


#####################################################################
# LOẠI NHẬP LIỆU
#####################################################################
INPUT_INPUT_TYPE_TEXT = 1
INPUT_INPUT_TYPE_ONE_CHOICE = 2
INPUT_INPUT_TYPE_MULTI_CHOICE = 3
INPUT_INPUT_TYPE_DATE = 4
INPUT_INPUT_TYPE_TIME = 5
INPUT_INPUT_TYPE_DATE_AND_TIME = 6
INPUT_INPUT_TYPE_MEDIA = 7
INPUT_INPUT_TYPE_DOCUMENT = 8
INPUT_INPUT_TYPE_RATING = 9
INPUT_INPUT_TYPE_RANGE = 10
INPUT_INPUT_TYPE_YES_NO_QUESTION = 11
INPUT_INPUT_TYPE_ON_OFF_FLAG = 12
INPUT_INPUT_TYPE_SIGNATURE = 13
INPUT_INPUT_TYPE_GROUP = 14

INPUT_TYPE = {
    INPUT_INPUT_TYPE_TEXT: _('Ô nhập'),
    INPUT_INPUT_TYPE_ONE_CHOICE: _('Một lựa chọn'),
    INPUT_INPUT_TYPE_MULTI_CHOICE: _('Nhiều lựa chọn'),
    INPUT_INPUT_TYPE_DATE: _('Ngày'),
    INPUT_INPUT_TYPE_TIME: _('Giờ'),
    INPUT_INPUT_TYPE_DATE_AND_TIME: _('Ngày & Giờ'),
    INPUT_INPUT_TYPE_MEDIA: _('Phương tiện'),
    INPUT_INPUT_TYPE_DOCUMENT: _('Tập tin'),
    INPUT_INPUT_TYPE_RATING: _('Đánh giá'),
    INPUT_INPUT_TYPE_RANGE: _('Phạm vi'),
    INPUT_INPUT_TYPE_YES_NO_QUESTION: _('Câu hỏi Đúng/Sai'),
    INPUT_INPUT_TYPE_ON_OFF_FLAG: _('Chuyển đổi Bật/Tắt'),
    INPUT_INPUT_TYPE_SIGNATURE: _('Chữ ký'),
    INPUT_INPUT_TYPE_GROUP: _('Nhóm'),
}
#####################################################################


#####################################################################
# ĐỊNH DẠNG CỦA LOẠI NHẬP LIỆU
#####################################################################

# Ô nhập
INPUT_TYPE_TEXT_FORMAT_NORMAL = 1  # Tự do
INPUT_TYPE_TEXT_FORMAT_CUSTOM = 2  # Tùy chỉnh

# Một lựa chọn
INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_DROPDOWN = 3  # Dropdown
INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_RADIO = 4  # Radio

# Nhiều lựa chọn
INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_DROPDOWN = 5  # Dropdown
INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_CHECKBOX = 6  # Checkbox

# Ngày
INPUT_INPUT_TYPE_DATE_FORMAT_NORMAL = 7  # Mặc định

# Giờ
INPUT_INPUT_TYPE_TIME_FORMAT_12HOUR = 8  # 12 giờ
INPUT_INPUT_TYPE_TIME_FORMAT_24HOUR = 9  # 24 giờ

# Ngày & Giờ
INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_12HOUR = 10  # 12 giờ
INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_24HOUR = 11  # 24 giờ

# Phương tiện
INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE = 12  # Hình ảnh
INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO = 13  # Video
INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND = 14  # Âm thanh

# Tệp tin
INPUT_INPUT_TYPE_DOCUMENT_FORMAT_FILE = 15  # Tệp tin
INPUT_INPUT_TYPE_DOCUMENT_FORMAT_ATTACH = 16  # Đính kèm
INPUT_INPUT_TYPE_DOCUMENT_FORMAT_LINK = 17  # Link

# Đánh giá
INPUT_INPUT_TYPE_RATING_FORMAT_STAR = 18  # Sao
INPUT_INPUT_TYPE_RATING_FORMAT_SCORE = 19  # Điểm

# Phạm vi
INPUT_INPUT_TYPE_RANGE_FORMAT_NORMAL = 20  # Mặc định

# Câu hỏi Đúng/Sai
INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_DROPDOWN = 21  # Dropdown
INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_RADIO = 22  # Danh sách

# Chuyển đổi Bật/Tắt
INPUT_INPUT_TYPE_ON_OFF_FLAG_FORMAT_NORMAL = 23  # Mặc định

# Chữ ký
INPUT_INPUT_TYPE_SIGNATURE_FORMAT_NORMAL = 24  # Mặc định

# Nhóm
INPUT_INPUT_TYPE_GROUP_FORMAT_NORMAL = 25  # Mặc định

INPUT_TYPE_FORMAT = {
    INPUT_TYPE_TEXT_FORMAT_NORMAL: _('Ô nhập định dạng tự do'),
    INPUT_TYPE_TEXT_FORMAT_CUSTOM: _('Ô nhập định dạng tùy chỉnh'),
    INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_DROPDOWN: _('Một lựa chọn định dạng dropdown'),
    INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_RADIO: _('Một lựa chọn định dạng radio'),
    INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_DROPDOWN: _('Nhiều lựa chọn định dạng dropdown'),
    INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_CHECKBOX: _('Nhiều lựa chọn định dạng checkbox'),
    INPUT_INPUT_TYPE_DATE_FORMAT_NORMAL: _('Ngày định dạng mặc định'),
    INPUT_INPUT_TYPE_TIME_FORMAT_12HOUR: _('Giờ định dạng 12 giờ'),
    INPUT_INPUT_TYPE_TIME_FORMAT_24HOUR: _('Giờ định dạng 24 giờ'),
    INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_12HOUR: _('Ngày & Giờ định dạng 12 giờ'),
    INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_24HOUR: _('Ngày & Giờ định dạng 24 giờ'),
    INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE: _('Phương tiện định dạng hình ảnh'),
    INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO: _('Phương tiện định dạng video'),
    INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND: _('Phương tiện định dạng âm thanh'),
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_FILE: _('Tệp tin định dạng tệp tin'),
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_ATTACH: _('Tệp tin định dạng đính kèm'),
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_LINK: _('Tệp tin định dạng link'),
    INPUT_INPUT_TYPE_RATING_FORMAT_STAR: _('Đánh giá định dạng sao'),
    INPUT_INPUT_TYPE_RATING_FORMAT_SCORE: _('Đánh giá định dạng điểm'),
    INPUT_INPUT_TYPE_RANGE_FORMAT_NORMAL: _('Phạm vi định dạng mặc định'),
    INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_DROPDOWN: _('Câu hỏi Đúng/Sai định dạng dropdown'),
    INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_RADIO: _('Câu hỏi Đúng/Sai định dạng radio'),
    INPUT_INPUT_TYPE_ON_OFF_FLAG_FORMAT_NORMAL: _('Chuyển đổi Bật/Tắt định dạng mặc định'),
    INPUT_INPUT_TYPE_SIGNATURE_FORMAT_NORMAL: _('Chữ ký định dạng mặc định'),
    INPUT_INPUT_TYPE_GROUP_FORMAT_NORMAL: _('Nhóm định dạng mặc định'),
}

INPUT_TYPE_FORMAT_CHOICE = ((k, v) for k, v in INPUT_TYPE_FORMAT.items())
INPUT_TYPE_FORMAT_LIST = [(k, v) for k, v in INPUT_TYPE_FORMAT.items()]


INPUT_TYPE_FORMAT_GROUP_BY_INPUT_TYPE = {
    INPUT_INPUT_TYPE_TEXT: [
        INPUT_TYPE_TEXT_FORMAT_NORMAL,
        INPUT_TYPE_TEXT_FORMAT_CUSTOM
    ],
    INPUT_INPUT_TYPE_ONE_CHOICE: [
        INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_DROPDOWN,
        INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_RADIO
    ],
    INPUT_INPUT_TYPE_MULTI_CHOICE: [
        INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_DROPDOWN,
        INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_CHECKBOX
    ],
    INPUT_INPUT_TYPE_DATE: [
        INPUT_INPUT_TYPE_DATE_FORMAT_NORMAL
    ],
    INPUT_INPUT_TYPE_TIME: [
        INPUT_INPUT_TYPE_TIME_FORMAT_12HOUR,
        INPUT_INPUT_TYPE_TIME_FORMAT_24HOUR
    ],
    INPUT_INPUT_TYPE_DATE_AND_TIME: [
        INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_12HOUR,
        INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_24HOUR
    ],
    INPUT_INPUT_TYPE_MEDIA: [
        INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE,
        INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO,
        INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND
    ],
    INPUT_INPUT_TYPE_DOCUMENT: [
        INPUT_INPUT_TYPE_DOCUMENT_FORMAT_FILE,
        INPUT_INPUT_TYPE_DOCUMENT_FORMAT_ATTACH,
        INPUT_INPUT_TYPE_DOCUMENT_FORMAT_LINK
    ],
    INPUT_INPUT_TYPE_RATING: [
        INPUT_INPUT_TYPE_RATING_FORMAT_STAR,
        INPUT_INPUT_TYPE_RATING_FORMAT_SCORE
    ],
    INPUT_INPUT_TYPE_RANGE: [
        INPUT_INPUT_TYPE_RANGE_FORMAT_NORMAL
    ],
    INPUT_INPUT_TYPE_YES_NO_QUESTION: [
        INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_DROPDOWN,
        INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_RADIO
    ],
    INPUT_INPUT_TYPE_ON_OFF_FLAG: [
        INPUT_INPUT_TYPE_ON_OFF_FLAG_FORMAT_NORMAL
    ],
    INPUT_INPUT_TYPE_SIGNATURE: [
        INPUT_INPUT_TYPE_SIGNATURE_FORMAT_NORMAL
    ],
    INPUT_INPUT_TYPE_GROUP: [
        INPUT_INPUT_TYPE_GROUP_FORMAT_NORMAL
    ],
}
#####################################################################

#####################################################################
# ĐIỀU KIỆN ĐI THEO TỪNG ĐỊNH DẠNG CỦA LOẠI NHẬP LIỆU
#####################################################################

INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT = 'text'  # Kiểu input
INPUT_TYPE_FORMAT_CONDITION_TYPE_DICT = 'dict'  # Kiểu nhiều cặp key, value
INPUT_TYPE_FORMAT_CONDITION_TYPE_RADIO = 'radio'  # Kiểu radio, group có nhiều option, nhưng chỉ được chọn 1
INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX = 'checkbox'
INPUT_TYPE_FORMAT_CONDITION_TYPE_NUMBER = 'number'
#####################################################################

INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_LIMIT_CHARACTER = 'limit_character'  # Giới hạn ký tự -> Check length text
INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA = 'enter_only_alpha'  # Chỉ cho phép nhập chữ cái
INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER = 'enter_only_number'  # Chỉ cho phép nhập số
INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MIN_NUMBER = 'min_number'
INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MAX_NUMBER = 'max_number'
INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_STEP = 'step'
INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT = 'enter_text'  # Cho phép nhập ký tự bất kỳ (bao gồm cả ký tự đặc biệt)
INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION = 'check_extension'  # Kiểm tra đuôi tệp tin
#####################################################################

INPUT_TYPE_FORMAT_CONDITION_ACTION = [
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_LIMIT_CHARACTER,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MIN_NUMBER,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MAX_NUMBER,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_STEP,
    INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION
]

# json condition cho kiểu ô nhập
INPUT_TYPE_TEXT_FORMAT_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Giới hạn ký tự'),
        'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_LIMIT_CHARACTER,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
        'value': '255'
    },
    {
        'checked_flag': None,
        'name': _('Cho phép nhập văn bản'),
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_RADIO,
        'action': None,
        'value': [
            {
                'checked_flag': False,
                'name': _('Chỉ văn bản'),
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': _('Chỉ số'),
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
                'type': None,
                'value': None
            },
            {
                'checked_flag': True,
                'name': _('Bao gồm các kí tự đặc biệt'),
                'action': INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT,
                'type': None,
                'value': None
            },
        ]
    }
]
#####################################################################

# json condition cho kiểu một lựa chọn hoặc nhiều lựa chọn
INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Nguồn dữ liệu'),
        'action': None,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_RADIO,
        'value': [
            {
                'checked_flag': False,
                'name': _('Nguồn'),
                'action': INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT,
                'type': None,
                'value': None
            },
            {
                'checked_flag': True,
                'name': _('Thủ công'),
                'action': None,
                'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_DICT,
                'value': None,
                'dict_value': {  # này là ngoại lệ cho INPUT_TYPE_FORMAT_CONDITION_TYPE_DICT
                    None: None
                }
            },
        ]
    }
]
#####################################################################


# json condition cho kiểu phương tiện loại định dạng hình ảnh
INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Định dạng'),
        'action': None,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX,
        'value': [
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_PNG,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_SVG,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_JPG,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_HEIC,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            }
        ]
    },
    {
        'name': _('Kích thước'),
        'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
        'value': ''
    }
]

# json condition cho kiểu phương tiện loại định dạng video
INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Định dạng'),
        'action': None,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX,
        'value': [
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_MP4,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_WMV,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_F4V,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_AVI,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_WEBM,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            }
        ]
    },
    {
        'name': _('Kích thước'),
        'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
        'value': ''
    }
]

# json condition cho kiểu phương tiện loại định dạng hình ảnh
INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Định dạng'),
        'action': None,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX,
        'value': [
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_MP3,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            }
        ]
    },
    {
        'name': _('Kích thước'),
        'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
        'value': ''
    }
]
#####################################################################


# json condition cho kiểu tệp tin
INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Loại'),
        'action': None,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX,
        'value': [
            {
                'checked_flag': False,
                'name': _('all'),
                'action': None,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_DOCX,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_DOC,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_XLS,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_PPTX,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_PDF,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_TXT,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_ZIP,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            },
            {
                'checked_flag': False,
                'name': FILE_EXTENSION_RAR,
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
                'type': None,
                'value': None
            }
        ]
    }
]
#####################################################################


# json condition cho kiểu đánh giá
INPUT_INPUT_TYPE_RATING_FORMAT_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Max'),
        'action': None,
        'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_NUMBER,
        'value': None
    }
]
#####################################################################


# json condition cho kiểu phạm vi
INPUT_INPUT_TYPE_RANGE_FORMAT_CONDITION_JSON = [
    {
        'checked_flag': None,
        'name': _('Giới hạn'),
        'action': None,
        'type': None,
        'value': [
            {
                'checked_flag': False,
                'name': _('Nhỏ nhất'),
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MIN_NUMBER,
                'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
                'value': None
            },
            {
                'checked_flag': False,
                'name': _('Lớn nhất'),
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MAX_NUMBER,
                'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
                'value': None
            },
            {
                'checked_flag': False,
                'name': _('Bước nhảy'),
                'action': INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_STEP,
                'type': INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
                'value': None
            }
        ]
    }
]
#####################################################################


INPUT_TYPE_FORMAT_CONDITION = {
    INPUT_TYPE_TEXT_FORMAT_NORMAL: INPUT_TYPE_TEXT_FORMAT_CONDITION_JSON,
    INPUT_TYPE_TEXT_FORMAT_CUSTOM: INPUT_TYPE_TEXT_FORMAT_CONDITION_JSON,

    INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_DROPDOWN: INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_ONE_CHOICE_FORMAT_RADIO: INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON,

    INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_DROPDOWN: INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_MULTI_CHOICE_FORMAT_CHECKBOX: INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON,

    INPUT_INPUT_TYPE_DATE_FORMAT_NORMAL: [],

    INPUT_INPUT_TYPE_TIME_FORMAT_12HOUR: [],
    INPUT_INPUT_TYPE_TIME_FORMAT_24HOUR: [],

    INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_12HOUR: [],
    INPUT_INPUT_TYPE_DATE_AND_TIME_FORMAT_24HOUR: [],

    INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE: INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE_CONDITION_JSON,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO: INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO_CONDITION_JSON,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND: INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND_CONDITION_JSON,

    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_FILE: INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_ATTACH: INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_LINK: INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON,

    INPUT_INPUT_TYPE_RATING_FORMAT_STAR: INPUT_INPUT_TYPE_RATING_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_RATING_FORMAT_SCORE: INPUT_INPUT_TYPE_RATING_FORMAT_CONDITION_JSON,

    INPUT_INPUT_TYPE_RANGE_FORMAT_NORMAL: INPUT_INPUT_TYPE_RANGE_FORMAT_CONDITION_JSON,

    INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_DROPDOWN: [],
    INPUT_INPUT_TYPE_YES_NO_QUESTION_FORMAT_RADIO: [],

    INPUT_INPUT_TYPE_ON_OFF_FLAG_FORMAT_NORMAL: [],

    INPUT_INPUT_TYPE_SIGNATURE_FORMAT_NORMAL: [],

    INPUT_INPUT_TYPE_GROUP_FORMAT_NORMAL: [],
}
#####################################################################
