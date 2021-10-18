from rest_framework import response
from library.constant.file_extension import (
    FILE_EXTENSION_DOCS,
    FILE_EXTENSION_IMAGES,
    FILE_EXTENSION_JPG,
    FILE_EXTENSION_PNG,
    FILE_EXTENSION_SOUNDS,
    FILE_EXTENSION_VIDEOS,
    FILE_EXTENSION_WMV,
)
from library.functions import string_to_datetime
import os
import re
from idm_config.settings import DATE_INPUT_FORMAT
from library.constant.input_type import (
    INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND,
    INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA,
    INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER,
)

from api.functions.template.userview_functions import get_data_from_output_api, parameter_list_to_string, validate_url

def validate_template_field_input_type_text(input_condition_json, value):
    condition = [condition_json for condition_json in input_condition_json[1]["value"] if condition_json["checked_flag"]][0]

    # Kiểm tra kiểu INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA
    if condition["action"] == INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_ALPHA:
        result = re.match(r"^[a-zA-Z]+$", value)
        if not result:
            return {"is_valid": False, "message": "`value` should be alphas [A-Z-a-z]"}

    # Kiểm tra kiểu INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER
    elif condition["action"] == INPUT_TYPE_FORMAT_CONDITION_ACTION_CHECK_ENTER_NUMBER:
        result = re.match(r"^\d*$", value)
        if not result:
            return {"is_valid": False, "message": "`value` should be digits [0-9]"}

    return {"is_valid": True, "message": ""}


def validate_template_field_input_type_one_or_multiple_choice(input_condition_json, api_third_party, value):
    condition_value = input_condition_json[0]["value"]
    response = []

    if condition_value[0]["checked_flag"] is True and condition_value[0]["name"] == "Nguồn":
        url = validate_url(api_third_party["url"], api_third_party["parameter_list"], api_third_party["method_type"], 
        api_third_party["token"], api_third_party["token_type"])

        if url == "":
            return {"is_valid": False, "message": "Can not get data form api third party"}

        url_info = url.split(",")
        try:
            response = get_data_from_output_api(url_info[0], int(url_info[1]), url_info[2], int(url_info[3]))
        except:
            return {"is_valid": False, "message": "Can not get data form api third party"}
    else:
        response = condition_value[1]["dict_value"]
    
    values = [item["value"] for item in response]

    if type(value) is list:
        for v in value:
            if v not in values:
                return {"is_valid": False, "message": f"value {v} not exists"}
    elif type(value) is str:
        if value not in values:
            return {"is_valid": False, "message": f"value {value} not exists"}
    
    return {"is_valid": True, "message": ""}


def validate_template_field_input_type_datetime(value: str, format=DATE_INPUT_FORMAT):
    convert = string_to_datetime(value, _format=format)
    if convert is None:
        return {"is_valid": False, "message": "Not true format"}
    return {"is_valid": True, "message": ""}


def validate_template_field_input_type_media(input_condition_json, value):
    try:
        format = str(value).upper().split(".")[-1]
        size = os.stat(value).st_size * pow(10,-6) # Get MB
    except Exception as ex:
        return {"is_valid": False, "message": f"File not true format"}

    if input_condition_json == INPUT_INPUT_TYPE_MEDIA_FORMAT_IMAGE:
        if format not in FILE_EXTENSION_IMAGES:
            return {"is_valid": False, "message": f"Not support format {format} in image files"}
    elif input_condition_json == INPUT_INPUT_TYPE_MEDIA_FORMAT_VIDEO:
        if format not in FILE_EXTENSION_VIDEOS:
            return {"is_valid": False, "message": f"Not support format {format} in video files"}
        return {"is_valid": True, "message": ""}
    elif input_condition_json == INPUT_INPUT_TYPE_MEDIA_FORMAT_SOUND:
        if format not in FILE_EXTENSION_SOUNDS:
            return {"is_valid": False, "message": f"Not support format {format} in sound files"}
        return {"is_valid": True, "message": ""}

    if size > float(input_condition_json[1]["value"]):
        return {"is_valid": False, "message": f"File tooo large"}

    return {"is_valid": True, "message": ""}


def validate_template_field_input_type_document(input_condition_json, value):
    try:
        format = str(value).upper().split(".")[-1]
    except Exception as ex:
        return {"is_valid": False, "message": f"File not true format"}

    if format not in FILE_EXTENSION_DOCS:
        return {"is_valid": False, "message": "Not support file with type {extension}"}

    return {"is_valid": True, "message": ""}


def validate_template_field_input_type_rating(input_condition_json, value):
    condition = input_condition_json[0]
    
    is_digit = value.isdigit()
    
    if is_digit is False:
        return {"is_valid": False, "message": "`value` must be digit"}

    max_value = float(condition["value"])
    if float(value) > max_value:
        return {"is_valid": False, "message": "value must to less than max value"}

    return {"is_valid": True, "message": ""}


def validate_template_field_input_type_range(input_condition_json, value):
    condition_value = input_condition_json[0]["value"]
    
    is_digit = value.isdigit()
    if is_digit is False:
        return {"is_valid": False, "message": "`value` must be digit"}
    
    value = float(value)

    min_number = float(condition_value[0]["value"])
    max_number = float(condition_value[1]["value"])
    step = float(condition_value[2]["value"])

    flag = value >= min_number and value <= max_number
    if flag is False:
        return {"is_valid": False, "message": "`value` must be greater than min number and less than max number"}

    return {"is_valid": True, "message": ""}

def validate_template_field_input_type_signature(input_condition_json, value):
    try:
        format = str(value).upper().split(".")[-1]
    except Exception as ex:
        return {"is_valid": False, "message": f"File not true format"}

    if format not in [FILE_EXTENSION_PNG, FILE_EXTENSION_JPG]:
        return {"is_valid": False, "message": "Not support file with type {extension}"}

    return {"is_valid": True, "message": ""}