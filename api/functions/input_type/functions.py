import json

from django.db.models.functions.text import Trim
from rest_framework.generics import RetrieveAPIView
from library.constant.file_extension import (
    FILE_EXTENSION_DOCS,
)
from library.constant.input_type import (
    INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_RANGE_FORMAT_CONDITION_JSON,
    INPUT_INPUT_TYPE_RATING_FORMAT_CONDITION_JSON,
    INPUT_TYPE_TEXT_FORMAT_CONDITION_JSON,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_LIMIT_CHARACTER, 
    INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT,
    INPUT_TYPE_FORMAT_CONDITION_TYPE_RADIO, 
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER, 
    INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT, 
    INPUT_TYPE_FORMAT_CONDITION_TYPE_DICT,
    INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION,
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MIN_NUMBER, 
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MAX_NUMBER, 
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_STEP,
    )
from library.functions import string_to_int

REQUIRED_KEYS_BASE = ['checked_flag', 'name', 'action', 'type', 'value']
REQUIRED_KEYS_SIZE = ['name', 'action', 'type', 'value']

def is_valid_input_type_text_format_condition(conditions: list) -> bool:
    if len(conditions) != len(INPUT_TYPE_TEXT_FORMAT_CONDITION_JSON):
        return False

    required_keys = ['checked_flag', 'name', 'action', 'type', 'value']

    # kiểm tra từng condition phải có đủ 5 field bên dưới
    for condition in conditions:
        for required_key in required_keys:
            if required_key not in condition:
                return False

    '''
    {
        "checked_flag": null,
        "name": "Giới hạn ký tự",
        "action": "limit_character",
        "type": "text",
        "value": "255"
    }
    '''
    first_condition = conditions[0]

    if isinstance(first_condition.get('action'), str) \
            and first_condition.get('action') != INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_LIMIT_CHARACTER:
        return False

    if first_condition.get('type') != INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT:
        return False

    number_limit_character = first_condition.get('value')
    if number_limit_character != '':
        if string_to_int(number_limit_character) <= 0:
            return False

    '''
    {
        "checked_flag": null,
        "name": "Cho phép nhập văn bản",
        "type": "radio",
        "action": null,
        "value": [
            {
                "checked_flag": false,
                "name": "Chỉ văn bản",
                "action": "enter_only_alpha",
                "type": null,
                "value": null
            },
            {
                "checked_flag": false,
                "name": "Chỉ số",
                "action": "enter_only_number",
                "type": null,
                "value": false
            },
            {
                "checked_flag": true,
                "name": "Bao gồm các kí tự đặc biệt",
                "action": "enter_text",
                "type": null,
                "value": null
            }
        ]
    }
    '''
    second_condition = conditions[1]

    if second_condition.get('type') != INPUT_TYPE_FORMAT_CONDITION_TYPE_RADIO:
        return False

    second_condition_values = second_condition.get('value')

    if not isinstance(second_condition_values, list):
        return False

    if len(second_condition_values) != len(INPUT_TYPE_TEXT_FORMAT_CONDITION_JSON[1]['value']):
        return False

    # vì radio nên trong list value cần có 1 checked_flag = True
    count_true_checked_flag = 0

    ordered_radio_actions = [
        INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA,
        INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
        INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT
    ]
    for index, second_condition_value in enumerate(second_condition_values):
        for required_key in required_keys:
            if required_key not in second_condition_value:
                return False

        second_condition_value_checked_flag = second_condition_value['checked_flag']
        second_condition_value_action = second_condition_value['action']

        if not isinstance(second_condition_value_checked_flag, bool) \
                or not isinstance(second_condition_value_action, str) \
                or second_condition_value_action != ordered_radio_actions[index]:
            return False

        if second_condition_value_checked_flag:
            count_true_checked_flag += 1

    if count_true_checked_flag != 1:
        return False

    return True

def _is_valid_required_keys(item, required_keys:list):
    for required_key in required_keys:
        if required_key not in item:
            return False
    return True

# lst can be conditions or values
def _is_valid_conditions_required_keys(lst:list, required_keys:list):
    for condition in lst:
        for required_key in required_keys:
            if required_key not in condition:
                return False
    return True

def _is_valid_conditions_len_and_required_keys(lst, constant_format, required_keys:list):
    if not isinstance(lst, list):
        return False

    if len(lst) != len(constant_format):
        return False

    if _is_valid_conditions_required_keys(lst, required_keys) is False:
        return False

    return True

def _is_validated_input_type_file_condition(condition, constant_intput_type_format, list_name_file_format: list):
    if condition["type"] != INPUT_TYPE_FORMAT_CONDITION_TYPE_CHECKBOX:
        return False

    value = condition["value"]
    if len(value) != len(constant_intput_type_format[0]["value"]):
        return False

    for v in value:
        if v['name'] not in list_name_file_format:
            return False
        if v['action'] != INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_EXTENSION:
            return False

    return True

def is_valid_input_type_one_or_multiple_choice_format_condition(conditions: list) -> bool:
    
    is_valid = _is_valid_conditions_len_and_required_keys(conditions,
        INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON, REQUIRED_KEYS_BASE)
    if is_valid == False:
        return False

    condition = conditions[0]
    type = condition["type"]
    value = condition["value"]

    if type != INPUT_TYPE_FORMAT_CONDITION_TYPE_RADIO:
        return False
    
    # Validated value:
    if not isinstance(value, list):
        return False
    
    if len(value) != len(INPUT_INPUT_TYPE_ONE_OR_MULTI_CHOICE_FORMAT_CONDITION_JSON[0]["value"]):
        return False

    # `value` have two child value must be validated
    first_value = value[0]
    second_value = value[1]

    # Check required:
    if _is_valid_required_keys(first_value, REQUIRED_KEYS_BASE) is False:
        return False

    required_keys = ['checked_flag', 'name', 'action', 'type', 'dict_value']
    if _is_valid_required_keys(second_value, required_keys) is False:
        return False
    
    # Check action:
    if first_value.get('action') != INPUT_TYPE_FORMAT_CONDITION_CHECK_ACTION_ENTER_TEXT:
        return False
    
    # Check type:
    if second_value.get('type') != INPUT_TYPE_FORMAT_CONDITION_TYPE_DICT:
        return False

    # Check dict value
    if not isinstance(second_value.get('dict_value'), dict):
        return False

    return True

def is_valid_input_type_media_format_condition(conditions: list, constant_intput_type_format, list_name_file_format: list) -> bool:

    # Condition 01
    first_condition = conditions[0]
    if _is_valid_required_keys(first_condition, REQUIRED_KEYS_BASE) is False:
        return False

    if _is_validated_input_type_file_condition(first_condition, constant_intput_type_format, list_name_file_format) is False:
        return False

    # Condition 2
    second_condition = conditions[1]
    if _is_valid_required_keys(second_condition, REQUIRED_KEYS_SIZE) is False:
        return False

    if second_condition['action'] != INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER:
        return False

    if second_condition['type'] != INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT:
        return False

    if str(second_condition['value']).isdigit() is False:
        return False

    return True

def is_valid_input_type_document_format_condition(conditions: list) -> bool:
    is_valid = _is_valid_conditions_len_and_required_keys(conditions, 
    INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON, REQUIRED_KEYS_BASE)
    if is_valid == False:
        return False

    condition = conditions[0]

    is_validated_condition = _is_validated_input_type_file_condition(condition, INPUT_INPUT_TYPE_DOCUMENT_FORMAT_CONDITION_JSON, FILE_EXTENSION_DOCS)
    
    if is_validated_condition == False:
        return False

    return True

def is_valid_input_type_range_format_condition(conditions: list) -> bool:
    is_valid = _is_valid_conditions_len_and_required_keys(conditions, 
    INPUT_INPUT_TYPE_RANGE_FORMAT_CONDITION_JSON, REQUIRED_KEYS_BASE)
    if is_valid == False:
        return False

    condition = conditions[0]
    value = condition["value"]

    if _is_valid_conditions_len_and_required_keys(value, INPUT_INPUT_TYPE_RANGE_FORMAT_CONDITION_JSON[0]["value"], REQUIRED_KEYS_BASE) is False:
        return False

    actions = [
        INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MIN_NUMBER, 
        INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_MAX_NUMBER, 
        INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_STEP]
    for v in value:
        if v["action"] not in actions:
            return False
        if v["type"] != INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT:
            return False
        if str(v['value']).isdigit() is False:
            return False

    return True

def is_valid_input_type_rating_format_condition(conditions: list) -> bool:
    is_valid = _is_valid_conditions_len_and_required_keys(conditions, 
    INPUT_INPUT_TYPE_RATING_FORMAT_CONDITION_JSON, REQUIRED_KEYS_BASE)
    if is_valid == False:
        return False

    condition = conditions[0]

    if condition["type"] != INPUT_TYPE_FORMAT_CONDITION_TYPE_TEXT:
        return False

    if str(condition['value']).isdigit() is False:
        return False

    return True