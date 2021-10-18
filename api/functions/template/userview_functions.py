import requests
import os
from io import BytesIO
import qrcode
import base64
from rest_framework import response
from rest_framework.fields import FileField
from library.constant.output_api import OUTPUT_API_METHOD_TYPE_GET, OUTPUT_AUTHORIZATION_API_TYPE

def get_data_from_output_api(url: str, method_type: int, token: str, token_type: int):
    # một vài trường hợp đặc biệt response có thể trả về text không phải json
    if token:
        if method_type == OUTPUT_API_METHOD_TYPE_GET:
            response = requests.get(
                url,
                verify=False,
                headers={"Authorization": OUTPUT_AUTHORIZATION_API_TYPE[token_type].split()[
                    0] + " " + token},
            ).json()

        else:
            response = requests.post(
                url,
                verify=False,
                headers={"Authorization": OUTPUT_AUTHORIZATION_API_TYPE[token_type].split()[
                    0] + " " + token},
            ).json()
    else:
        if method_type == OUTPUT_API_METHOD_TYPE_GET:
            response = requests.get(
                url,
                verify=False,
            ).json()

        else:
            response = requests.post(
                url,
                verify=False,
            ).json()

    return response

def upload_file_to_service(self,file_name):
    url = SERVICE_FILE_API_FILES_URL

    file_byte = BytesIO(file_name.read())
    
    files = {'file': file_byte}
    headers_api = SERVICE_FILE_HEADER
    
    response = requests.post(
        url,
        verify=False, 
        files=files, 
        headers=headers_api)
  
    if response.status_code != status.HTTP_201_CREATED:
        return self.http_exception('error file to server')

    res = response.json()
    return res

def parameter_list_to_string(url: str, parameter_list: list):
    parameter_list_string_list = []
    parameter_string = ""
    if parameter_list:
        for parameter in parameter_list:
            param = f'{parameter["key"]}={parameter["value"]}'
            parameter_list_string_list.append(param)
        parameter_string = "?" + "&".join(parameter_list_string_list)
    return url + parameter_string

def validate_url(url: str, output_parameter_list: list, c_output_method_type: str,  output_token: str, output_authorization_api_token_type: str):
    url = parameter_list_to_string(url, output_parameter_list)
    if url == "":
        return url

    flag = c_output_method_type is not None
    flag = output_token != ""
    flag = output_authorization_api_token_type is not None
    if flag:
        url += ',' + str(c_output_method_type)
        url += ',' + str(output_token)
        url += ',' + str(output_authorization_api_token_type)
        if "null" not in url:
            return url
    return ""

def save_file_local(file_uuid: FileField, folder):
    path = os.path.join(folder, str(file_uuid))
    with open(path, 'wb+') as f:
        for chunk in file_uuid.chunks():
            f.write(chunk)
    return path


def generate_qr_code(code: str):
    # Create QR Code Image (PIL Image)
    image = qrcode.make(code)

    #Convert PIL Image to Byte
    buffered = BytesIO()
    image.save(buffered, format="JPEG")

    #Convert Byte to Base64 string
    img_str = base64.b64encode(buffered.getvalue())
    data = base64.encodebytes(img_str).decode('utf-8')

    return data