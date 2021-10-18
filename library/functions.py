import json
import re
from datetime import date, datetime
from typing import Optional

from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import status

#from library.constant.service_file import SERVICE_FILE_HEADER, SERVICE_FILE_API_FILES

from idm_config.root_local import SERVICE_FILE_URL
from idm_config.settings import DATETIME_INPUT_OUTPUT_FORMAT
import requests


def decode_to_json(data):
    return json.loads(data)


def today():
    return date.today()


def now():
    return datetime.now()


def datetime_to_string(_time: datetime, _format=DATETIME_INPUT_OUTPUT_FORMAT) -> str:
    if _time:
        return _time.strftime(_format)
    return ''


def string_to_datetime(string: str, default=None, _format=DATETIME_INPUT_OUTPUT_FORMAT) -> datetime:
    try:
        return datetime.strptime(string, _format)
    except (ValueError, TypeError):
        return default


def string_to_int(string: str, default=None) -> int:
    try:
        return int(string)
    except (ValueError, TypeError):
        return default


def date_to_datetime(date_input: date, default=None) -> datetime:
    try:
        return datetime.combine(date_input, datetime.min.time())
    except (ValueError, TypeError):
        return default


def datetime_to_date(datetime_input: datetime, default=None) -> date:
    try:
        return datetime_input.date()
    except (ValueError, TypeError):
        return default


def end_time_of_day(datetime_input: datetime, default=None) -> datetime:
    try:
        return datetime_input.replace(hour=23, minute=59, second=59)
    except (ValueError, TypeError):
        return default


def is_valid_url(url):
    pattern = r"^(https|http)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$"
    if re.match(pattern, url):
        return True
    else:
        return False


def upload_file_service(file: InMemoryUploadedFile) -> Optional[str]:
    url = f'{SERVICE_FILE_URL}/{SERVICE_FILE_API_FILES}'
    headers_api = SERVICE_FILE_HEADER

    file_data = {'file': file}

    try:
        response = requests.post(
            url,
            verify=False,
            files=file_data,
            headers=headers_api
        )

        if response.status_code != status.HTTP_201_CREATED:
            return None

        res = response.json()
        return res['uuid']

    except requests.exceptions.RequestException:
        return None


def download_multi_file_from_service(uuids: list) -> Optional[list]:
    url = f'{SERVICE_FILE_URL}/{SERVICE_FILE_API_FILES}'
    headers_api = SERVICE_FILE_HEADER

    dict_uuid = {'uuid': uuids}

    try:
        response = requests.get(
            url,
            verify=False,
            params=dict_uuid,
            headers=headers_api,
        )
        if response.status_code != status.HTTP_200_OK:
            return None

        list_res = []

        for res in response.json():
            list_res.append(res['file_url'])

        return list_res

    except requests.exceptions.RequestException:
        return None

#
def remove_spaces_str_and_upper(string):
    return ''.join(string.split()).upper()

def diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def string_to_date_dmy(self, date):
    try:
        date = '{} 00:00:00'.format(date, '%d-%m-%Y %H:%M:%S')
        return datetime.strptime(date, '%d/%m/%Y %H:%M:%S')
    except:
        return self.http_exception("date type is date %d/%m/%Y")